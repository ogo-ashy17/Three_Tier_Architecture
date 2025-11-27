import streamlit as st

st.title("Rename App Folder Example")

st.write("This is a simple Streamlit app to demonstrate renaming the application folder.")  

st.text_input("Enter your name:", key="name_input")

st.text_area("Enter your bio:", key="bio_input", height=350)

st.button("Submit")