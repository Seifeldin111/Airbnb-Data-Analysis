import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.data import load_data, apply_global_filters

st.set_page_config(page_title="EDA", page_icon="🔍")

st.header("Exploratory Data Analysis")


# Check if data is loaded
if "fdf" not in st.session_state or st.session_state["fdf"] is None:
    st.warning("⚠️ Please upload a dataset first on the Data Source page.")
    st.stop()


st.subheader("Overview")


#  Use persisted data
df = st.session_state["fdf"]
st.write(df.head())



st.info("These charts will reflect the filters applied in the sidebar.")


st.session_state.fdf = apply_global_filters(st.session_state["raw_df"])








st.header("1. Neighborhood Group Analysis")


col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# Count of listings by neighbourhood group
with col1:
    fig, ax = plt.subplots(figsize=(6,4))
    df['neighbourhood_group'].value_counts().plot(kind='bar')
    ax.set_xlabel("Neighbourhood Group")
    ax.set_ylabel("Count")
    ax.set_title("Listings by Neighbourhood Group")
    st.pyplot(fig)


# Number of Reviews by neighbourhood group
with col2:
    fig, ax = plt.subplots(figsize=(6,4))
    df.groupby('neighbourhood_group')['number_of_reviews'].mean().plot(kind='bar')
    ax.set_title("Mean No. of Reviews by Neighbourhood Group")
    ax.set_ylabel("No. of Reviews")
    ax.set_xlabel("Neighbourhood Group")
    st.pyplot(fig)



# Average Approx Profit by neighbourhood group
with col3:
    fig, ax = plt.subplots(figsize=(6,4))
    df.groupby('neighbourhood_group')['approx_profit'].mean().plot(kind='bar')
    ax.set_title("Mean Approx. Profit by Neighbourhood Group")
    ax.set_ylabel("Approx. Profit")
    ax.set_xlabel("Neighbourhood Group")
    st.pyplot(fig)



# Average Price by neighbourhood group
with col4:
    fig, ax = plt.subplots(figsize=(6, 4))
    df.groupby('neighbourhood_group')['price'].mean().plot(kind='bar')
    ax.set_title("Mean Price by Neighbourhood Group")
    ax.set_ylabel("Price")
    ax.set_xlabel("Neighbourhood Group")
    st.pyplot(fig)




# --- Markdown Insights ---
st.markdown(
    """
    ### Insights Neighborhood Groups Analysis

    - **Staten Island** has the **lowest number of listings** compared to all other neighborhood groups, with a **huge difference**.  
    - Despite that, it has the **highest number of reviews**.  
    - It also ranks **third in Reviews-to-Price ratio**, with only a very small gap compared to the top groups.  

    **Implication:**  
    Staten Island generates **nearly the same revenue as other neighborhood groups** despite having far fewer listings.  

    If the number of listings in Staten Island increases, the overall revenue is very likely to increase as well.  
    """
)
















st.header("2. Neighborhood Group & Room Type Analysis")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))  # 2 rows, 2 cols

# 1. Number of Listings by Neighborhood Group & Room Type
sns.countplot(data=df, x="neighbourhood_group", hue="room_type", ax=axes[0,0])
axes[0,0].set_title("Number of Listings by Neighbourhood Group and Room Type")
axes[0,0].set_xlabel("Neighbourhood Group")
axes[0,0].set_ylabel("Count of Listings")
axes[0,0].legend(title="Room Type")

# 2. Avg Price by Neighborhood Group & Room Type
sns.barplot(data=df, x="neighbourhood_group", y="price", hue="room_type", ci=None, ax=axes[0,1])
axes[1,1].set_title("Avg Price by Neighbourhood Group and Room Type")
axes[1,1].set_xlabel("Neighbourhood Group")
axes[1,1].set_ylabel("Avg Price")
axes[1,1].legend(title="Room Type")

# 3. Avg Approx Profit by Neighborhood Group & Room Type
if "approx_profit" in df.columns:
    sns.barplot(data=df, x="neighbourhood_group", y="approx_profit", hue="room_type", ci=None, ax=axes[1,0])
    axes[1,0].set_title("Avg Approx Profit by Neighbourhood Group and Room Type")
    axes[1,0].set_xlabel("Neighbourhood Group")
    axes[1,0].set_ylabel("Avg Approx Profit")
    axes[1,0].legend(title="Room Type")

# 4. Avg Number of Reviews by Neighborhood Group & Room Type
sns.barplot(data=df, x="neighbourhood_group", y="number_of_reviews", hue="room_type", ci=None, ax=axes[1,1])
axes[0,1].set_title("Avg Number of Reviews by Neighbourhood Group and Room Type")
axes[0, 1].set_xlabel("Neighbourhood Group")
axes[0,1].set_ylabel("Avg Reviews")
axes[0, 1].legend(title="Room Type")

plt.tight_layout()
st.pyplot(fig)





st.markdown("""
### Insights from Neighborhood Group & Room Type Analysis

- In **Manhattan**, although the **Entire Home/Apartment** room type is the most common, it has the **least number of reviews** (even fewer than Shared Rooms).  
- Its slightly higher value in terms of **Approximate Profit** comes mainly from its **much higher price** compared to the other two room types, not because of stronger demand.  
- This suggests that in **Manhattan**, it would be better to **invest more in Private Rooms** rather than Entire Homes.  

- On the other hand, in the **other four Neighborhood Groups** (Brooklyn, Queens, Bronx, Staten Island), the pattern is **opposite**:  
  - Although the number of **Entire Home/Apartment** listings is smaller than Private Rooms,  
  - They receive **more reviews** and achieve a **higher Approximate Profit**.  
  - This implies that in these four groups, it would be better to **increase the number of Entire Homes**.  
  

- Interestingly, we also observed that although the **number of listings for Shared Rooms** is very low across all five neighborhood groups, the **number of reviews for Shared Rooms is surprisingly high**, sometimes **competing with or even exceeding other room types**, especially in **Manhattan**.  
  This implies that **expanding Shared Rooms in Manhattan** could be a promising strategy.  
""")












st.header("3. Minimum Charge Analysis")


c1, c2 = st.columns(2)
with c1:
    min_charge_reviews = df.groupby('minimum_charge')['number_of_reviews'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(min_charge_reviews['minimum_charge'], min_charge_reviews['number_of_reviews'])
    ax.set_title("Average Number of Reviews by Minimum Charge")
    ax.set_xlabel("Minimum Charge ($)")
    ax.set_ylabel("Average Number of Reviews")
    ax.grid()
    st.pyplot(fig)

with c2:
    min_charge_profit = df.groupby('minimum_charge')['approx_profit'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(min_charge_profit['minimum_charge'], min_charge_profit['approx_profit'])
    ax.set_title("Average Approx. Profit by Minimum Charge")
    ax.set_xlabel("Minimum Charge ($)")
    ax.set_ylabel("Average Approx. Profit")
    ax.grid()
    st.pyplot(fig)







st.markdown("""
### Insights from Minimum Charge Analysis
When plotting **Minimum Charge** on the x-axis against either **Number of Reviews** or **Approximate Profit** on the y-axis, we observed a clear trend:

Higher reviews and higher Approximate Profit values tend to occur at **relatively lower Minimum Charges**.
Only a few exceptions deviate from this trend.
This suggests that **affordable listings tend to attract more bookings and better performance in terms of revenue**.
""")









import matplotlib.pyplot as plt

st.header("4. Host Listings Analysis")

c1, c2 = st.columns(2)

with c1:
    host_profit = df.groupby('calculated_host_listings_count')['approx_profit'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(host_profit['calculated_host_listings_count'], host_profit['approx_profit'], marker='o')
    ax.set_title("Average Approx. Profit by Host Listings Count")
    ax.set_xlabel("Calculated Host Listings Count")
    ax.set_ylabel("Average Approx. Profit")
    ax.grid()
    st.pyplot(fig)

with c2:
    host_reviews = df.groupby('calculated_host_listings_count')['number_of_reviews'].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(host_reviews['calculated_host_listings_count'], host_reviews['number_of_reviews'], marker='o')
    ax.set_title("Average Number of Reviews by Host Listings Count")
    ax.set_xlabel("Calculated Host Listings Count")
    ax.set_ylabel("Average Number of Reviews")
    ax.grid()
    st.pyplot(fig)




st.markdown("""
### Insights from Host Listings Count Analysis
We observed that both **Approximate Profit** and **Number of Reviews** decrease as the **Host Listings Count** increases beyond a certain threshold (around 50 listings).

Possible explanations include:

Guests may **trust large-scale hosts less**, preferring smaller or individual hosts.
Hosts with many listings may **struggle to maintain quality**, leading to fewer reviews and lower performance.
""")












st.header("5. Coastal vs Non-Coastal")


agg = df.groupby('coastal', as_index=False).agg(
    listings=('price','size'),
    total_reviews=('number_of_reviews','sum'),
    avg_price=('price','mean'),
    avg_approx_profit=('approx_profit','mean')
)

# Map labels
label_map = {0:'Non-Coastal', 1:'Coastal'}
agg['area'] = agg['coastal'].map(label_map)










fig, axes = plt.subplots(2, 2, figsize=(12, 10))  # 2 rows, 2 cols


# 1. Number of listings
sns.countplot(x='coastal', data=df, ax=axes[1,1])
axes[0,0].set_title("Number of Listings")
axes[0,0].set_xlabel("Coastal (1) vs Non-Coastal (0)")
axes[0,0].set_ylabel("Count")

# 2. Average price
sns.barplot(x='coastal', y='price', data=df, ax=axes[0,1], ci=None)
axes[1,1].set_title("Avg Price")
axes[1,1].set_xlabel("Coastal (1) vs Non-Coastal (0)")
axes[1,1].set_ylabel("Price")

# 3. Average approx_profit (if available)
if "approx_profit" in df.columns:
    sns.barplot(x='coastal', y='approx_profit', data=df, ax=axes[1,0], ci=None)
    axes[1,0].set_title("Avg Approx Profit")
    axes[1,0].set_xlabel("Coastal (1) vs Non-Coastal (0)")
    axes[1,0].set_ylabel("Profit")

# 4. Average number of reviews
sns.barplot(x='coastal', y='number_of_reviews', data=df, ax=axes[0,0], ci=None)
axes[0, 1].set_title("Avg Number of Reviews")
axes[0, 1].set_xlabel("Coastal (1) vs Non-Coastal (0)")
axes[0,1].set_ylabel("Reviews")

plt.tight_layout()
st.pyplot(fig)


st.subheader("Insights from Coastal vs Non-Coastal listings")
st.markdown("""
We found that the **number of listings** is higher in **coastal areas** compared to non-coastal areas.
However:

The **number of reviews** is greater in non-coastal areas despite having fewer listings.
The **Approximate Profit** is slightly higher for coastal areas, mainly due to much higher prices rather than higher review engagement.
This suggests that **non-coastal areas may be a better investment opportunity**, as they attract more reviews relative to their smaller number of listings, indicating stronger demand and engagement despite fewer listings.
""")