import streamlit as st
from glob import glob

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
for page_link in glob('pages/*.py'):
    st.page_link(page_link)
