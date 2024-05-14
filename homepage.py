import streamlit as st

st.set_page_config(
    page_title="Gallery Homepage"
)

st.write("# Experimental Video Generation gallery")
st.sidebar.success("Select a tab")

st.markdown(
    """Homepage to gallery for better navigation of model inference, 
    enables smoother naviagtion rather than stiching GIFs together, compressing it's information"""
)

st.write("Link to the pages")
st.page_link('pages/new_page.py', label="512 results")
