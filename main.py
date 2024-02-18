import streamlit as st
num1 = st.number_input("Enter the Number 1")
num2 = st.number_input("Enter the Number 2")
if st.button("Add"):
    st.write(f"# {num1+num2}")
    st.balloons()
st.file_uploader("Upload a CSV")