import streamlit as st
import pandas as pd
from utils import load_data, plot_ghi_boxplot

st.set_page_config(
    page_title="Solar Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f2027 0%, #2c5364 100%);
        animation: gradientShift 10s infinite;
    }
    .glass {
        background: rgba(40, 40, 60, 0.7);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        padding: 2rem;
        margin-bottom: 2rem;
        transition: transform 0.3s;
    }
    .glass:hover {
        transform: scale(1.02);
    }
    @keyframes gradientShift {
        0% {
            background-position: 0% 50%;
        }
        50% {
            background-position: 100% 50%;
        }
        100% {
            background-position: 0% 50%;
        }
    }
    @media (max-width: 600px) {
        .glass {
            padding: 1rem;
        }
    }
    .loading {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 200px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Solar Resource Dashboard")


countries = ["Benin", "SierraLeone", "Togo"]
selected_countries = st.sidebar.multiselect(
    "Select countries", countries, default=countries, key="country_select"
)
ghi_range = st.sidebar.slider(
    "Filter GHI Range (W/m²)", 0, 1200, (0, 1200), key="ghi_slider")


@st.cache_data
def load_and_filter_data(selected_countries, ghi_range):
    """Loads and filters data, now with caching."""
    df = load_data(selected_countries)
    if not df.empty:  
        df = df[(df["GHI"] >= ghi_range[0]) & (df["GHI"] <= ghi_range[1])]
    return df

with st.spinner("Loading and filtering data..."):
    df = load_and_filter_data(selected_countries, ghi_range)


st.subheader("Key Metrics")
if df.empty:
    st.warning("No data available for the selected countries and GHI range.")
else:
    col1, col2, col3 = st.columns(3)
    metrics = ["GHI", "DNI", "DHI"]
    for i, metric in enumerate(metrics):
        with [col1, col2, col3][i]:
            avg_value = df[metric].mean()
            data_range = df[metric].max() - df[metric].min()
            st.metric(
                label=f"Avg {metric}",
                value=f"{avg_value:.1f} W/m²",
                delta=f"{data_range:.1f} range",
                delta_color="off"
            )

    st.subheader("GHI Distribution by Country")
    st.markdown(
        "<div class='glass'>"
        "<b>Boxplot:</b> Visualizing the spread and central tendency of GHI for each selected country.",
        unsafe_allow_html=True
    )
    plot_ghi_boxplot(df)

st.markdown('</div>', unsafe_allow_html=True)
