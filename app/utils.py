import pandas as pd
import streamlit as st
import plotly.express as px  
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(selected_countries):
    dfs = []
    try:
        for country in selected_countries:
            file = f"data/{country.lower()}_clean.csv"
            df = pd.read_csv(file)
            df["Country"] = country
            dfs.append(df)
        return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()
    except FileNotFoundError:
        st.error("Data files not found. Ensure CSV files are in the data/ folder.")
        return pd.DataFrame()


def plot_ghi_boxplot(df, toggle=False):
    if df.empty:
        st.info("No data to display.")
        return
    
    fig = px.box(
        df,
        x="Country",
        y="GHI",
        color="Country",  
        color_discrete_sequence=[
            "rgba(54, 162, 235, 0.8)",
            "rgba(255, 206, 86, 0.8)",
            "rgba(255, 99, 132, 0.8)",
            "rgba(75, 192, 192, 0.8)",
            "rgba(153, 102, 255, 0.8)",
        ], 
        labels={"GHI": "GHI (W/m²)"},  
        title="GHI Distribution by Country",
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",  
        paper_bgcolor="rgba(0,0,0,0)",  
        font_color="white",
        boxmode="overlay", 
    )

    st.plotly_chart(fig, use_container_width=True)
