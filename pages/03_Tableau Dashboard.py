import streamlit as st

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")



st.markdown(
    """
    <h1 style="text-align: center; margin-bottom: 40px;">
        📊 Interactive Tableau Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)



st.markdown(
    """
    <style>
    .tableau-embed iframe {
        transform: scale(0.8);   /* zoom out */
        transform-origin: 0 0;   /* top-left corner */
        width: 200%;             /* compensate for scale */
        height: 1200px;
    }
    </style>
    <div class="tableau-embed">
        <iframe src="https://public.tableau.com/views/AirbnbDashboardV3/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no"
                width="1300" height="1200"></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
