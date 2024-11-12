import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Hi! Welcome to my Car Eval Web App!👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    This web app was created to perform an analysis on a car evaluation dataset.
    As well as to create a machine learning model to help classify car evals in the future!

    To navigate this web app to view the analysis of the dataset or use the machine learning model,
    please use the navigation bar on the left! Thank you!
"""
)