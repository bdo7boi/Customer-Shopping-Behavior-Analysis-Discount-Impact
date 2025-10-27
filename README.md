*******Shopper Behavior Analysis — Impact of Discounts on AOV*********


*****Project Overview*********

This project analyzes shopper behavior to understand how product discounts influence Average Order Value (AOV) across different product categories.
The goal was to identify which categories actually benefit from discounts and which experience AOV erosion, providing actionable insights for e-commerce pricing strategy.

Using Python (Pandas, NumPy, SciPy) for data processing and Tableau for visualization, the analysis follows a complete data-to-insight workflow — from cleaning and aggregation to business interpretation and visual storytelling.

*******Objectives**********

- Evaluate how discounts affect purchasing behavior across product categories.
- Identify which categories see higher order values under discounting.
- Highlight areas where discounts fail to drive meaningful sales lift (AOV erosion).
- Provide evidence-based recommendations for targeted discount strategies.

**********Dataset************

Source: Shopper Behavior Dataset [(publicly available on Kaggle)](https://www.kaggle.com/datasets/rehan497/customer-shopping-behavior-dataset).
The dataset includes transactional records such as:

- Category – product type (e.g., Accessories, Footwear, Outerwear)
- Purchase Amount (USD) – order value per transaction
- Discount Applied – binary indicator of whether the purchase included a discount

Each transaction was analyzed to compare discounted vs. non-discounted orders within each product category.


******Analysis Workflow**********

1. Data Cleaning & Preparation
  - Loaded and cleaned the dataset using Pandas.
  - Normalized discount indicators (Yes/No → 1/0).
  - Removed incomplete or malformed records.
2. Feature Engineering
  - Grouped data by Category and Discount Status.
  - Calculated key performance metrics:
    - Average Order Value (AOV)
    - Difference (Δ AOV) and Percent Lift
- Conducted Welch’s t-test and computed Hedges’ g to measure the magnitude of the discount effect.
3. Visualization & Insights
  - Exported summarized metrics to CSV.
  - Built visual dashboards in Tableau highlighting:
    - Categories with AOV Lift (positive response to discounts).
    - Categories with AOV Erosion (negative response).

Key Findings
Category	AOV Impact	Insight
Footwear	↑ +4.6%	Discounts slightly increase spending — suitable for seasonal sales.
Accessories	↓ –4.0%	Discounts reduce AOV — customers likely buy low-priced items on sale.
Outerwear	↓ –5.5%	AOV erosion suggests discounts aren’t driving higher-value orders.
Clothing	–1.0%	Minimal change — discounts have negligible impact.

*********Business Implications***********
- Targeted discounting: Focus promotions on Footwear, where discounts increase customer spend.
- Margin protection: Avoid heavy discounting on Accessories and Outerwear, as it reduces average order value.
- Future testing: Consider A/B tests on limited categories to validate AOV lift and conversion trade-offs.

*********Tools Used***********
- Python: Data cleaning, aggregation, and statistical analysis (Pandas, NumPy, SciPy).
- Tableau: Dashboard creation for interactive visual storytelling.
- Matplotlib: Supporting visual exports for portfolio visualization.


<img width="1786" height="1098" alt="image" src="https://github.com/user-attachments/assets/15f53718-6e32-4871-826c-1aa38e47d2c0" />



Link to full dashboard: https://public.tableau.com/views/CustomerBehaviorDiscountImpactAnalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
