import streamlit as st
import pandas as pd
from streamlit import session_state
from utils.data import load_data, apply_global_filters

st.set_page_config(page_title="Airbnb NYC Analysis", page_icon="📤", layout="wide")

st.title("Airbnb NYC: Revenue & Review Insights")    

st.markdown("""
This Streamlit app wraps our full analysis: problem definition, EDA, geographic comparisons, host strategy,
room type insights, and an embedded Tableau dashboard. Use the sidebar to filter globally.
""")


if "raw_df" not in st.session_state:
    st.session_state["raw_df"] = None




# Data source
st.markdown("---")
st.subheader("Data Source")


up = st.file_uploader("Upload Airbnb CSV", type=["csv"])
if up is not None:
    if st.session_state["raw_df"] is None:
        st.session_state["raw_df"] = load_data(up)
    st.success("✅ Data loaded and saved to session")
else:
    st.info("Please upload a CSV file to continue.")





if 'raw_df' in session_state and st.session_state["raw_df"] is not None:

    st.session_state.fdf = apply_global_filters(st.session_state["raw_df"])

    # KPI cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Total Listings", f"{len(st.session_state.fdf):,}")
    with c2:
        if 'number_of_reviews' in st.session_state.fdf.columns:
            st.metric("Total Reviews", f"{int(st.session_state.fdf['number_of_reviews'].sum()):,}")
    with c3:
        if 'price' in st.session_state.fdf.columns:
            st.metric("Avg Price", f"$ {st.session_state.fdf['price'].mean():.0f}")
    with c4:
        if 'approx_profit' in st.session_state.fdf.columns:
            st.metric("Avg Review-Price", f"$ {st.session_state.fdf['approx_profit'].mean():,.0f}")

    st.markdown("""
    **Navigation:** use the Pages menu (left) to open specific analyses: Overview, EDA, Coastal vs Non-Coastal,
    Hosts, Room Types, and the Tableau Dashboard.
    """)

