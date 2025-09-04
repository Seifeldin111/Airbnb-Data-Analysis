import pandas as pd
import numpy as np
import streamlit as st

@st.cache_data(show_spinner=True)
def load_data(csv_path: str) -> pd.DataFrame:
    df = pd.read_csv(csv_path)

    expected = ['neighbourhood_group','neighbourhood','room_type','price',
                'minimum_nights','number_of_reviews','availability_365','latitude','longitude']
    missing = [c for c in expected if c not in df.columns]
    if missing:
        st.warning(f"Missing expected columns: {missing}. The app may have limited functionality.")

    for c in ['price','minimum_nights','number_of_reviews','availability_365','latitude','longitude']:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')


    # Data Cleaning

    # Dropping any entries with a price less than 0
    df = df[df['price'] > 0]

    # Removing Outliers in price
    df = df[df['price'] < 334]

    df.dropna(inplace=True)

    # Removing outliers in minimum_nights
    df = df[df['minimum_nights'] <= 365]

    # Removing Outliers in number_of_reviews
    df = df[df['number_of_reviews'] < 500]

    df.drop(['name', 'host_id'], axis=1, inplace=True)





    # Feature Engineering

    # Feature: Approx_Revenue
    if 'price' in df.columns and 'number_of_reviews' in df.columns:
        df['approx_profit'] = df['number_of_reviews'] * df['price']

    # Feature: coastal vs non-coastal
    def is_coastal(lat, lon):
        if lon < -73.95 or lon > -73.85 or lat < 40.6 or lat > 40.85:
            return 1
        else:
            return 0
    df['coastal'] = df.apply(lambda row: is_coastal(row['latitude'], row['longitude']), axis=1)

    # Feature: minimum_charge
    if 'minimum_nights' in df.columns and 'price' in df.columns:
        df['minimum_charge'] = df['minimum_nights'] * df['price']



    # Removing outliers in minimum_charge
    df = df[df['minimum_charge'] < 150000]


    return df






def apply_global_filters(df):
    st.sidebar.header("Global Filters")

    # Neighborhood group filter
    if 'neighbourhood_group' in df.columns:
        groups = sorted(df['neighbourhood_group'].dropna().unique().tolist())
        sel_groups = st.sidebar.multiselect(
            "Neighbourhood Group",
            options=groups,
            default=groups,
            key="filter_neighbourhood_group"
        )
        st.session_state["sel_groups"] = sel_groups

        if sel_groups:
            df = df[df['neighbourhood_group'].isin(sel_groups)]

    # Room type
    if 'room_type' in df.columns:
        rtypes = df['room_type'].dropna().unique().tolist()
        sel_rtypes = st.sidebar.multiselect(
            "Room Type",
            sorted(rtypes),
            default=st.session_state.get("sel_rtypes", sorted(rtypes)),
            key="filter_room_type"
        )
        st.session_state["sel_rtypes"] = sel_rtypes
        df = df[df['room_type'].isin(sel_rtypes)]

    # Price range
    if 'price' in df.columns:
        min_p, max_p = float(np.nanmin(df['price'])), float(np.nanmax(df['price']))
        sel_min, sel_max = st.sidebar.slider(
            "Price range",
            min_value=0.0, max_value=max(100.0, max_p),
            value=st.session_state.get("price_range", (0.0, max_p)),
            key="filter_price"
        )
        st.session_state["price_range"] = (sel_min, sel_max)
        df = df[(df['price'] >= sel_min) & (df['price'] <= sel_max)]

    return df
