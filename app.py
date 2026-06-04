import streamlit as st
import pandas as pd
from analysis import *

st.set_page_config(
    page_title="Cricket Data Analyzer",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 Cricket Data Analysis Dashboard")

uploaded_file = st.file_uploader(
    "Upload Cricket CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("CSV Uploaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.write(f"Rows: {df.shape[0]}")
    st.write(f"Columns: {df.shape[1]}")

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Overview",
            "Batting Analysis",
            "Bowling Analysis",
            "Team Analysis"
        ]
    )

    with tab1:
        dataset_overview(df)

    with tab2:
        batting_analysis(df)

    with tab3:
        bowling_analysis(df)

    with tab4:
        team_analysis(df)
