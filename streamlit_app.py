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
st.write(response)

st.video(response['records'][0]['clip_sample']['url'])