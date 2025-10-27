
#Category x Discount impact on order value (AOV) — simplified portfolio version
#
#What it does:
#- Loads CSV
#- Encodes Discount Applied -> discount_flag (0/1)
#- Per Category: AOV with vs without discount
#- Welch's t-test (independent samples, unequal variance)
#- Hedges' g (effect size)
#- Outputs a clean CSV and optional charts






import pandas as pd
import numpy as np
from pathlib import Path
from scipy import stats
import matplotlib.pyplot as plt

# -----------------------------
# Config
# -----------------------------
INPUT_CSV = Path("shopping_behavior_updated.csv")
OUTPUT_CSV = Path("category_discount_impact.csv")
MIN_PER_GROUP = 10         # min sample size in BOTH groups to run stats
MAKE_CHARTS = True         # set False to skip chart creation
TOP_N = 10                 # how many categories to show in charts

# -----------------------------
# Helpers
# -----------------------------
def make_discount_flag(s: pd.Series) -> pd.Series:
    """Normalize Discount Applied to a 0/1 flag. Non-yes -> 0."""
    mapping = {
        "yes": 1, "y": 1, "true": 1, "1": 1,
        "no": 0, "n": 0, "false": 0, "0": 0,
    }
    return (
        s.astype(str).str.strip().str.lower()
         .map(mapping).fillna(0).astype(int)
    )

def hedges_g(a: np.ndarray, b: np.ndarray) -> float:
    """Hedges' g effect size (positive = discount has higher mean)."""
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    n1, n0 = a.size, b.size
    if n1 < 2 or n0 < 2:
        return np.nan
    s1 = a.std(ddof=1)
    s0 = b.std(ddof=1)
    df = n1 + n0 - 2
    if df <= 0:
        return np.nan
    sp = np.sqrt(((n1 - 1) * s1**2 + (n0 - 1) * s0**2) / df)
    if sp == 0:
        return np.nan
    d = (a.mean() - b.mean()) / sp
    # small-sample correction
    J = 1 - (3 / (4 * (n1 + n0) - 9)) if (n1 + n0) > 9 else 1.0
    return d * J

# -----------------------------
# Load & basic clean
# -----------------------------
df = pd.read_csv(INPUT_CSV)

need = ["Category", "Purchase Amount (USD)", "Discount Applied"]
missing = [c for c in need if c not in df.columns]
if missing:
    raise ValueError(f"Missing required column(s): {missing}")

df["Purchase Amount (USD)"] = pd.to_numeric(df["Purchase Amount (USD)"], errors="coerce")
df = df.dropna(subset=["Purchase Amount (USD)", "Category", "Discount Applied"])
df["discount_flag"] = make_discount_flag(df["Discount Applied"])

# -----------------------------
# Category-level calculations
# -----------------------------
rows = []
for cat, sub in df.groupby("Category"):
    disc = sub.loc[sub["discount_flag"] == 1, "Purchase Amount (USD)"].to_numpy()
    nods = sub.loc[sub["discount_flag"] == 0, "Purchase Amount (USD)"].to_numpy()

    n1, n0 = disc.size, nods.size
    aov1 = float(np.nan) if n1 == 0 else float(np.mean(disc))
    aov0 = float(np.nan) if n0 == 0 else float(np.mean(nods))

    delta = np.nan
    pct_lift = np.nan
    if n1 > 0 and n0 > 0:
        delta = aov1 - aov0
        pct_lift = ((aov1 / aov0) - 1) * 100 if aov0 != 0 else np.nan

    # Welch’s t-test + Hedges’ g only if both groups have enough data
    t_stat = np.nan
    p_val = np.nan
    g = np.nan
    if n1 >= MIN_PER_GROUP and n0 >= MIN_PER_GROUP:
        t_stat, p_val = stats.ttest_ind(disc, nods, equal_var=False, nan_policy="omit")
        g = hedges_g(disc, nods)

    rows.append({
        "Category": cat,
        "N_discount": int(n1),
        "N_no_discount": int(n0),
        "AOV_discount": aov1,
        "AOV_no_discount": aov0,
        "Delta_AOV": delta,
        "Pct_Lift": pct_lift,
        "Welch_t": t_stat,
        "p_value": p_val,
        "Hedges_g": g
    })

result = pd.DataFrame(rows)

# Clean up formatting (optional)
num_cols = ["AOV_discount","AOV_no_discount","Delta_AOV","Pct_Lift","Welch_t","p_value","Hedges_g"]
for c in num_cols:
    if c in result.columns:
        result[c] = result[c].astype(float).round(4)

# Sort by % lift (largest positive first)
result = result.sort_values("Pct_Lift", ascending=False)

# Save CSV
OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
result.to_csv(OUTPUT_CSV, index=False)
print("\n=== Category x Discount Impact (Top by % Lift) ===")
print(result.head(10).to_string(index=False))
print(f"\nSaved results to: {OUTPUT_CSV.resolve()}")


# -----------------------------
if MAKE_CHARTS:
    # ensure enough data: min of the two groups as a quick quality filter
    result["_min_n"] = result[["N_discount","N_no_discount"]].min(axis=1)

    top = result.dropna(subset=["Pct_Lift"]).query("_min_n >= @MIN_PER_GROUP").nlargest(TOP_N, "Pct_Lift")
    bot = result.dropna(subset=["Pct_Lift"]).query("_min_n >= @MIN_PER_GROUP").nsmallest(TOP_N, "Pct_Lift")

    if not top.empty:
        plt.figure(figsize=(8,5))
        plt.bar(top["Category"], top["Pct_Lift"])
        plt.title("Top Categories by % AOV Lift with Discount")
        plt.ylabel("% Lift in AOV (Discount vs No Discount)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("top_lift_categories.png")
        plt.close()
        print("Saved: top_lift_categories.png")

    if not bot.empty:
        plt.figure(figsize=(8,5))
        plt.bar(bot["Category"], bot["Pct_Lift"])
        plt.title("Categories with AOV Erosion from Discount")
        plt.ylabel("% Lift in AOV (Discount vs No Discount)")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig("erosion_categories.png")
        plt.close()
        print("Saved: erosion_categories.png")

    # clean up helper column
    result.drop(columns=["_min_n"], inplace=True, errors="ignore")

    if __name__ == "__main__":
        main()
