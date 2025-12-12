

import streamlit as st
import pandas as pd

st.title("2) Top N + Select Columns")

file = st.file_uploader("Upload empinfo.csv", type=["csv"])
if not file:
    st.stop()

df = pd.read_csv(file)

n = st.slider("How many rows to show?", 5, 200, 20)
cols = st.multiselect("Select columns", df.columns.tolist(), default=df.columns.tolist())

st.dataframe(df[cols].head(n))
