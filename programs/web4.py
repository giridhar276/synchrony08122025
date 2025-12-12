
import streamlit as st

st.title("Example 6: Tabs & Expanders")

tab1, tab2, tab3 = st.tabs(["Overview", "Details", "Settings"])

with tab1:
    st.write("This is the Overview tab.")

with tab2:
    st.write("Detailed information goes here.")

with tab3:
    st.write("Settings related content.")

with st.expander("Click to see FAQs"):
    st.write("Q1: ...")
    st.write("Q2: ...")