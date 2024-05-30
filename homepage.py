import streamlit as st
from glob import glob
import re


st.set_page_config(
    page_title="Gallery Homepage"
)

st.write("# Experimental Video Generation gallery")
st.sidebar.success("Select a tab")

st.markdown(
    """Homepage to gallery for better navigation of model inference.
    
    Note: Incase the app throws an error in any tab, try refreshing 
    it since the application interacts with the databse only once 
    so any change done at the moment might casue an error with old cache"""
)

st.subheader(":blue[OpenSora V1.0 Experiments]")
for v1_match in glob('pages/*OS_V1.0*.py'):
    st.page_link(v1_match)

st.subheader(":green[OpenSora V1.1 Experiments]")
for v1_1_match in glob('pages/*OS_V1.1*.py'):
    st.page_link(v1_1_match)

# st.page_link('pages/Upload_New_Page.py')
