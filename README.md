# Shopper Behavior — Discount Impact on AOV (by Category)

This project measures how discounts affect **Average Order Value (AOV)** across product **categories**, using a public shopper behavior dataset.  
It answers a practical question: **Which categories actually see higher order value when discounted—and which ones suffer margin erosion?**

## How it works
- **Python (Pandas/NumPy/Scipy)** computes AOV with vs. without discount per category.
- Uses **Welch’s t-test** (unequal variances) and **Hedges’ g** (effect size).
- Exports a clean results table and two simple charts.

## Key files
- `analysis/category_discount_impact.py` — executable script (simple, portfolio-ready).
- `results/category_discount_impact.csv` — final table with AOV, Δ, % lift, p-value, effect size.
- `results/erosion_categories.png` — categories where discounts reduce AOV.
- `results/top_lift_categories.png` — categories with positive % AOV lift from discount.

# Run (expects data/shopping_behavior_updated.csv unless you pass --input)
python analysis/category_discount_impact.py --input data/shopping_behavior_updated.csv --outdir results


<img width="1786" height="1098" alt="image" src="https://github.com/user-attachments/assets/15f53718-6e32-4871-826c-1aa38e47d2c0" />



Link to full dashboard: https://public.tableau.com/views/CustomerBehaviorDiscountImpactAnalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
