import streamlit as st
import pandas as pd
from utils import load_data, plot_ghi_boxplot

st.set_page_config(
    page_title="Solar Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Minimalist CSS for a clean look
st.markdown("""
    <style>
    .main {
        background-color: #1e1e1e;
        padding: 1rem;
    }
    .container {
        background-color: #2b2b2b;
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    .stSidebar {
        background-color: #2b2b2b;
    }
    h1, h2, h3 {
        color: #ffffff;
    }
    @media (max-width: 600px) {
        .container {
            padding: 1rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

st.title("Solar Dashboard")

# Sidebar for country selection
countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select Countries", countries, default=countries, key="country_select"
)

# Load and filter data
df = load_data(selected_countries)
if df.empty or "GHI" not in df.columns:
    st.error("Unable to load data or 'GHI' column not found. Ensure CSV files (e.g., benin_clean.csv) are uploaded to the data/ folder in Streamlit Community Cloud. If running locally, place them in the data/ folder.")
else:
    st.markdown('<div class="container">', unsafe_allow_html=True)

    # Key Metrics
    st.subheader("Key Metrics")
    col1, col2, col3 = st.columns(3)
    metrics = ["GHI", "DNI", "DHI"]
    for i, metric in enumerate(metrics):
        if metric in df.columns:
            with [col1, col2, col3][i]:
                avg_value = df[metric].mean()
                data_range = df[metric].max() - df[metric].min()
                st.metric(
                    label=f"Average {metric}",
                    value=f"{avg_value:.1f} W/m²",
                    delta=f"{data_range:.1f} range",
                    delta_color="off"
                )

    # GHI Boxplot
    st.subheader("GHI Distribution by Country")
    plot_ghi_boxplot(df)

    # Top Regions Table (Toggleable)
    if st.checkbox("Show Top Regions by GHI"):
        st.subheader("Top Regions by Average GHI")
        if "Region" in df.columns:
            top = df.groupby(["Country", "Region"])["GHI"].mean().reset_index()
            top = top.sort_values("GHI", ascending=False).head(5)
            st.dataframe(top)
        else:
            st.info("No region data available.")

    st.markdown('</div>', unsafe_allow_html=True)
