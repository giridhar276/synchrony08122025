

import streamlit as st
import pandas as pd

st.title("4) Filter by Workclass")

file = st.file_uploader("Upload empinfo.csv", type=["csv"])
if not file:
    st.stop()

df = pd.read_csv(file)

choices = ["All"] + sorted(df["workclass"].dropna().unique().tolist())
pick = st.selectbox("Workclass", choices)

filtered = df if pick == "All" else df[df["workclass"] == pick]
st.write("Rows:", len(filtered))
st.dataframe(filtered)
