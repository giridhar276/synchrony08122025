import streamlit as st

st.title("Example 2: Basic Widgets")

if st.button("Click Me"):
    st.write("Button was clicked!")

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You agreed!")

choice = st.radio(
    "Choose your favorite language:",
    ["Python", "R", "Julia"]
)
st.write(f"You selected: **{choice}**")