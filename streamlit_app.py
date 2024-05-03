import streamlit as st
from st_xatadb_connection import XataConnection
import requests

st.set_page_config(page_title='Xata Demo',layout='wide')
xata = st.connection('xata',type=XataConnection)

st.title('🖼️ Gallery demo')
st.caption("Powered by Xata")
st.divider()
# if "Images" not in st.session_state or st.session_state.Images is None:
    # st.session_state["Images"] = [xata.query("OS_gens",{"page":{ "size": 6}, "sort": {"xata.createdAt": "desc"}})]

response = xata.query('OS_gens', {"page":{"size": 3}})
cols = st.columns(3)
for column_index, clip_sample in enumerate(response['records']):
    cols[column_index%3].video(clip_sample['clip_sample']['url'])