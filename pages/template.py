import streamlit as st
from st_xatadb_connection import XataConnection


class Page_Template():

    def __init__(self, page_id, page_title='OS_Results'):
        self.page_id = page_id
        self.page_title = page_title

    def launch_page(self):
        # st.set_page_config(page_title=self.page_title,layout='wide')
        xata = st.connection('xata',type=XataConnection)

        # if "Data" not in st.session_state or st.session_state.Data is None:
        #     st.session_state["Data"] = [xata.query("OS_gens", {"sort": {"expt_id": "asc"}})]
        # if "expt_id" not in st.session_state:
        #     st.session_state['expt_id']=1
        try:
            st.session_state['expt_id']=self.page_id
            st.session_state["Data"] = [xata.query("OS_gens", {"filter": {"expt_id": st.session_state['expt_id']}})]
            # gallery_title = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]['expt_name']
            metadata = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]

        except:
            st.session_state['expt_id']=-1
            st.session_state["Data"] = [xata.query("OS_gens", {"filter": {"expt_id": st.session_state['expt_id']}})]
            metadata = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]


        st.title(metadata['expt_name'])
        if metadata['metadata'] != "No data":
            st.markdown(metadata['metadata'])
        # st.caption("Custom Pipeline dataset (5M training clips) 16frames@24fps")
        # st.divider()

        # response = xata.query('OS_gens', {"page":{"size": 3}})
        # response = xata.query('OS_gens')
        cols = st.columns(3)
        column_index = 0
        for clip_sample in st.session_state['Data'][0]['records']:
            if clip_sample['expt_id'] == st.session_state['expt_id']:
                cols[column_index%3].video(clip_sample['clip_sample']['url'], loop=False, autoplay=True)
                column_index += 1

    def launch_page_V2(self):
        # st.set_page_config(page_title=self.page_title,layout='wide')
        xata = st.connection('xata',type=XataConnection)
        try:
            st.session_state['expt_id']=self.page_id
            st.session_state["Data"] = [xata.query("OS_results_new_format", {"filter": {"expt_id": st.session_state['expt_id']}})]
            # gallery_title = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]['expt_name']
            metadata = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]

        except:
            st.session_state['expt_id']=-1
            st.session_state["Data"] = [xata.query("OS_gens", {"filter": {"expt_id": st.session_state['expt_id']}})]
            metadata = xata.query("ExperimentTitle", {"filter":{"expt_id":st.session_state['expt_id']}})['records'][0]


        st.title(metadata['expt_name'])
        if metadata['metadata'] != "No data":
            st.markdown(metadata['metadata'])

        cols = st.columns(3)
        column_index = 0
        if st.session_state['Data'][0]['records'][0]['expt_id'] == st.session_state['expt_id']:
            for clip_sample in st.session_state['Data'][0]['records'][0]['Videos']:
                cols[column_index%3].video(clip_sample['url'], loop=False, autoplay=True)
                column_index += 1

st.header("End of the line!")