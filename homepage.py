import streamlit as st
from glob import glob

st.set_page_config(
    page_title="Gallery Homepage"
)

st.write("# Experimental Video Generation gallery")
st.sidebar.success("Select a tab")

st.markdown(
    """Homepage to gallery for better navigation of model inference, 
    enables smoother naviagtion rather than stiching GIFs together, compressing it's information.
    
    Note: Incase the app throws an error in any tab, try refreshing 
    it since the application interacts with the databse only once 
    so any change done at the moment might casue an error with old cache"""
)

st.write("Link to the pages")
for page_link in glob('pages/[0-9]*.py'):
    if page_link != "pages/__init__.py":
        st.page_link(page_link)
# st.page_link('pages/Upload_New_Page.py')
