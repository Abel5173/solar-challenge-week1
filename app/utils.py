import pandas as pd
import streamlit as st
import plotly.express as px


def load_data(selected_countries):
    dfs = []
    for country in selected_countries:
        file = f"data/{country.lower()}_clean.csv"
        try:
            df = pd.read_csv(file)
            df["Country"] = country
            dfs.append(df)
        except FileNotFoundError:
            st.warning(
                f"Data file for {country} not found at {file}. If deployed, ensure the file is uploaded to Streamlit Community Cloud.")
            continue
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()


def plot_ghi_boxplot(df):
    if df.empty or "GHI" not in df.columns:
        st.info("No data to display or 'GHI' column missing.")
        return
    fig = px.box(
        df,
        x="Country",
        y="GHI",
        color="Country",
        labels={"GHI": "GHI (W/m²)"},
        title="GHI Distribution by Country"
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_font_color="white",
        boxmode="overlay"
    )
    st.plotly_chart(fig, use_container_width=True)
