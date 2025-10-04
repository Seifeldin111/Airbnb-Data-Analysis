import streamlit as st

st.set_page_config(page_icon="🏙️")

# Project Overview Title
st.markdown(
    """
    <h1 style="text-align: center; margin-bottom: 30px;">
        📝 Project Overview
    </h1>
    """,
    unsafe_allow_html=True
)

# Problem Definition Section
st.markdown(
    """
    ### 📌 Problem Definition  
    The core objective of this project is to **identify how Airbnb can increase its revenue and optimize its market presence in New York City** by analyzing patterns across neighborhood groups, room types, host activity, and geographic locations.  

    Specifically, we aim to:  

    - **Detect** neighborhoods and room types that offer the highest return potential relative to their number of listings.  
    - **Identify** areas where pricing or marketing strategies can improve performance.  
    - **Understand** how host behavior (e.g., number of listings per host) impacts guest engagement.  
    - **Explore** the geographic dimension (coastal vs non-coastal) to reveal opportunities for expansion.  

    By addressing these points, **Airbnb can make data-driven decisions** on:  
    - Where to expand  
    - Which listing types to prioritize  
    - How to adjust pricing strategies for maximum revenue growth   
    """,
    unsafe_allow_html=True
)

