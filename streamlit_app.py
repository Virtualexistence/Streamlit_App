import streamlit as st
import pandas as pd
from io import StringIO

tab_list = ['Draft Tab', 'Reserve tab']
reserve_list = tab_list.copy()

st.button("Reset", type="primary")
if st.button("Add a tab"):
    tab_list.append(f'New Tab {len(tab_list)}')
else:
    tab_list = reserve_list



tabs = st.tabs(tab_list)

with tabs[0]:
    cols = st.columns(3)
    uploaded_files = st.file_uploader("Upload the files to visualise", accept_multiple_files=True, key = 0)
    if uploaded_files is not None:
        for col_index, uploaded_file in enumerate(uploaded_files):
            with cols[col_index % 3]:
                st.video(uploaded_file,loop=True, autoplay=True)

with tabs[1]:
    cols = st.columns(3)
    uploaded_files = st.file_uploader("Upload the files to visualise", accept_multiple_files=True, key = 1)
    if uploaded_files is not None:
        for col_index, uploaded_file in enumerate(uploaded_files):
            with cols[col_index % 3]:
                st.video(uploaded_file,loop=True, autoplay=True)