

import streamlit as st
import pandas as pd

st.title("1) Read CSV + Show Data")

file = st.file_uploader("Upload empinfo.csv", type=["csv"])
if file:
    df = pd.read_csv(file)
    st.success(f"Loaded: {df.shape[0]} rows × {df.shape[1]} cols")
    st.dataframe(df)
else:
    st.info("Upload a CSV to continue.")
