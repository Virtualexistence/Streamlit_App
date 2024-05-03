import streamlit as st
from st_xatadb_connection import XataConnection
import requests

st.set_page_config(page_title='Xata Demo',layout='wide')
xata = st.connection('xata',type=XataConnection)

st.title('VidGen Gallery 🎑')
st.caption("Powered by Xata")
st.divider()

if "Data" not in st.session_state or st.session_state.Data is None:
    st.session_state["Data"] = [xata.query("OS_gens")]

# response = xata.query('OS_gens', {"page":{"size": 3}})
# response = xata.query('OS_gens')
cols = st.columns(3)
for column_index, clip_sample in enumerate(st.session_state['Data']['records']):
    cols[column_index%3].video(clip_sample['clip_sample']['url'])