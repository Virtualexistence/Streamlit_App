import streamlit as st
import pandas as pd
from io import StringIO

uploaded_files = st.file_uploader("Upload the files to visualise", accept_multiple_files=True)
if uploaded_files is not None:
    for uploaded_file in uploaded_files:
        st.video(uploaded_file,loop=True, autoplay=True)