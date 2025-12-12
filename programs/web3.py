

import streamlit as st

st.title("Example 3: Input Widgets")

city = st.selectbox(
    "Select a city",
    ["Hyderabad", "Bangalore", "Mumbai", "Delhi"]
)
st.write("City selected:", city)

hobbies = st.multiselect(
    "Select your hobbies",
    ["Reading", "Cycling", "Gym", "Music", "Travel"]
)
#st.write("Hobbies:", hobbies)

age = st.slider("Select your age", min_value=18, max_value=60, value=30)
st.write(f"Age: {age}")

name = st.text_input("Enter your name", value="Guest")
st.write(f"Hello, **{name}** ")

