import streamlit as st
from st_xatadb_connection import XataConnection
import requests

st.set_page_config(page_title='OS_Results',layout='wide')
xata = st.connection('xata',type=XataConnection)

if "Data" not in st.session_state or st.session_state.Data is None:
    st.session_state["Data"] = [xata.query("OS_gens", {"sort": {"expt_id": "asc"}})]
if "expt_id" not in st.session_state:
    st.session_state['expt_id']=0


st.title('VidGen Gallery 🎑')
st.caption("Powered by Xata - Free Plan")
try:
    gallery_title = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]['expt_name']
except:
    st.session_state['expt_id']=0
    gallery_title = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]['expt_name']


st.header(gallery_title, divider=True)
# st.divider()

# response = xata.query('OS_gens', {"page":{"size": 3}})
# response = xata.query('OS_gens')
cols = st.columns(3)
column_index = 0
for clip_sample in st.session_state['Data'][0]['records']:
    if clip_sample['expt_id'] == st.session_state['expt_id']:
        cols[column_index%3].video(clip_sample['clip_sample']['url'], loop=True, autoplay=True)
        column_index += 1
             
button_columns = st.columns([0.5, 0.5])

if button_columns[0].button("Previous", use_container_width=True):
    if st.session_state['expt_id'] > 0:
        st.session_state['expt_id'] -= 1
        st.rerun()

if button_columns[1].button("Next", use_container_width=True):
        st.session_state['expt_id'] += 1
        st.rerun()
