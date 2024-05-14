import streamlit as st
from glob import glob
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Gallery Homepage"
)

st.write("# Dev Homepage | Local testing ")
st.sidebar.success("Select a page")

st.markdown(
    """Homepage to gallery for better navigation of model inference, 
    enables smoother naviagtion rather than stiching GIFs together, compressing it's information"""
)

st.write("Link to the pages")
for page_link in glob('pages/[0-9]*.py'):
    if page_link is not "pages/__init__.py":
        st.page_link(page_link)
st.page_link('pages/Upload_New_Page.py')
