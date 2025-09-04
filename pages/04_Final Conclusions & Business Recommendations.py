import streamlit as st

st.set_page_config(page_title="Final Conclusions & Recommendations", page_icon="📈")

st.title("📊 Final Conclusions & Business Recommendations")

st.markdown("""
## **Key Insights from the Analysis**

### 1. Staten Island’s Untapped Potential
- Staten Island has the **lowest number of listings** compared to all other neighborhood groups.  
- **Despite this, it has one of the highest number of reviews**, ranking **3rd in Reviews-to-Price ratio**, very close to the top.  
- **Implication:** Staten Island is **under-supplied**. Increasing listings here is highly likely to boost overall revenue.

---

### 2. Manhattan Room Type Dynamics
- In Manhattan, **Entire Homes/Apartments dominate in number of listings**.  
- However, they record **the lowest number of reviews**, even **less than Shared Rooms**.  
- Their slightly higher Review-to-Price ratio comes **only from higher prices**, not higher demand.  
- **Recommendation:**  
  - Focus investments on **Private Rooms** in Manhattan.  
  - Reduce reliance on Entire Homes.  

---

### 3. Other Neighborhood Groups (Brooklyn, Queens, Bronx, Staten Island)
- The opposite pattern emerges here:  
  - **Entire Homes** generate more reviews and higher Review-Price ratios than Private Rooms.  
- **Recommendation:**  
  - Increase the supply of **Entire Homes** in these areas.  

---

### 4. Minimum Charge vs. Performance
- Listings with **lower Minimum Charges** consistently attract **more reviews** and achieve **better Review-to-Price ratios**.  
- Only a few exceptions deviate from this trend.  
- **Recommendation:** Keep listings **affordable** to maximize demand and performance.  

---

### 5. Host Listing Count and Trust
- Both **Review-Price and Number of Reviews drop** once a host manages more than **~50 listings**.  
- **Possible reasons:**  
  - Guests may prefer smaller or individual hosts due to **trust issues**.  
  - Quality may **decline with scale**, leading to lower reviews.  
- **Recommendation:** Focus on **quality over quantity**. Avoid excessively scaling the number of listings per host.  

---

### 6. Coastal vs Non-Coastal Listings
- **Coastal areas:**  
  - Have more listings.  
  - Higher Review-Price ratio, but this is mostly due to **much higher prices**, not higher engagement.  
- **Non-Coastal areas:**  
  - Have fewer listings.  
  - But generate **more reviews**, showing stronger demand and guest interaction.  
- **Recommendation:** Invest more in **non-coastal areas**, which demonstrate higher engagement despite smaller supply.  

---

## **Business Recommendations Summary**
- ✅ **Expand listings in Staten Island**: strong demand despite low supply.  
- ✅ **Prioritize Private Rooms in Manhattan** over Entire Homes.  
- ✅ **Increase Entire Home listings in Brooklyn, Queens, Bronx, and Staten Island.**  
- ✅ **Keep prices affordable** (lower Minimum Charge → higher demand & performance).  
- ✅ **Limit host scale per individual** to maintain trust and quality.  
- ✅ **Focus on non-coastal areas** for better guest engagement and sustainable demand.  

---

## **Limitations of the Analysis**
- ❌ We did not have the **exact number of bookings per listing**; reviews were used as a **proxy for demand**.  
- ❌ The analysis does not account for **time trends** in demand.  

---

## **Overall Conclusion**
The data suggests clear opportunities to **rebalance investments** across room types, neighborhood groups, and pricing strategies.  
By focusing on **Staten Island growth, non-coastal expansion, Private Rooms in Manhattan, and affordability across listings**, the business can **maximize both demand and revenue** while maintaining quality and trust.  
""")
