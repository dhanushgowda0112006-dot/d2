import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def dataset_overview(df):

    st.subheader("Dataset Information")

    info = pd.DataFrame({
        "Column": df.columns,
        "Datatype": df.dtypes.astype(str),
        "Missing Values": df.isnull().sum()
    })

    st.dataframe(info)

    st.subheader("Statistics")
    st.dataframe(df.describe(include="all"))


def batting_analysis(df):

    st.subheader("Batting Analysis")

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numerical columns found")
        return

    selected = st.selectbox(
        "Select Batting Metric",
        numeric_cols
    )

    fig, ax = plt.subplots()

    ax.hist(df[selected].dropna(), bins=20)

    ax.set_title(selected)

    st.pyplot(fig)

    st.write(df[selected].describe())


def bowling_analysis(df):

    st.subheader("Bowling Analysis")

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        st.warning("No numerical columns found")
        return

    selected = st.selectbox(
        "Select Bowling Metric",
        numeric_cols,
        key="bowling"
    )

    fig, ax = plt.subplots()

    ax.boxplot(df[selected].dropna())

    ax.set_title(selected)

    st.pyplot(fig)

    st.write(df[selected].describe())


def team_analysis(df):

    st.subheader("Team Analysis")

    cat_cols = df.select_dtypes(include="object").columns

    if len(cat_cols) == 0:
        st.warning("No categorical columns found")
        return

    selected = st.selectbox(
        "Select Team Column",
        cat_cols
    )

    counts = df[selected].value_counts()

    st.dataframe(counts)

    fig, ax = plt.subplots()

    counts.head(10).plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(f"Top 10 {selected}")

    st.pyplot(fig)
