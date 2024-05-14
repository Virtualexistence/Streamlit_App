import os, re
import streamlit as st
from glob import glob

def sanitize_filename(filename):
    # Define a regular expression pattern for invalid characters
    invalid_chars = r'[<>:"/\\|?*\']'
    # Replace invalid characters with an underscore or any other preferred character
    sanitized_filename = re.sub(invalid_chars, '_', filename)
    return sanitized_filename

file_id = len(os.listdir('pages'))-2
st.write("After uploading reload the page to refresh the cache. This'll avoid error due to any changes since the app interacts with the database only once during the initiation.")
tab_name = st.chat_input("Untitled Tab")
if tab_name:
    f_name = f"{file_id}_{sanitize_filename(tab_name).replace(".", "_")}.py"

    with open(os.path.join('pages' ,f_name), 'w') as filename:
        filename.write(f"""from pages.template.template import Page_Template

stage_settings = Page_Template({file_id-1})

stage_settings.launch_page()""")
        
    st.rerun()