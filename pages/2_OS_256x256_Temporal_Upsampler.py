import streamlit as st
from st_xatadb_connection import XataConnection
import requests

st.set_page_config(page_title='OS_Results',layout='wide')
xata = st.connection('xata',type=XataConnection)

# if "Data" not in st.session_state or st.session_state.Data is None:
#     st.session_state["Data"] = [xata.query("OS_gens", {"sort": {"expt_id": "asc"}})]
# if "expt_id" not in st.session_state:
#     st.session_state['expt_id']=1

st.session_state['expt_id']=1
st.session_state["Data"] = [xata.query("OS_gens", {"filter": {"expt_id": st.session_state['expt_id']}})]

# st.title('VidGen Gallery 🎑')
# st.caption("Powered by Xata - Free Plan")

gallery_title = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]['expt_name']



st.title(gallery_title)
st.caption("Custom Pipeline dataset (5M training clips) 16frames@24fps")
# st.divider()

# response = xata.query('OS_gens', {"page":{"size": 3}})
# response = xata.query('OS_gens')
cols = st.columns(3)
column_index = 0
for clip_sample in st.session_state['Data'][0]['records']:
    if clip_sample['expt_id'] == st.session_state['expt_id']:
        cols[column_index%3].video(clip_sample['clip_sample']['url'], loop=False, autoplay=True)
        column_index += 1