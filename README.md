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


# Run (expects data/shopping_behavior_updated.csv unless you pass --input)
python analysis/category_discount_impact.py --input data/shopping_behavior_updated.csv --outdir results



<div class='tableauPlaceholder' id='viz1761547601531' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cu&#47;CustomerBehaviorDiscountImpactAnalysis&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='CustomerBehaviorDiscountImpactAnalysis&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Cu&#47;CustomerBehaviorDiscountImpactAnalysis&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1761547601531');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='777px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>


Link to full dashboard: https://public.tableau.com/views/CustomerBehaviorDiscountImpactAnalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
