import pickle
import json
import streamlit as st
import pandas as pd

# load already saved files
with open("data/transcribed_table", "rb") as fp:
    transcribed_table = pickle.load(fp)

with open("data/summaries.json", "rb") as fp:
    summaries = json.load(fp)

with open("data/displacy.txt", "r") as file:
    displacy_response = file.read()

# load it as a dataframe
df = pd.DataFrame(transcribed_table)

st.title("Transcription Demo")
st.audio("data/audio_sample2.mp3")

if st.button("transcribe audio"):
    st.table(transcribed_table)

    for i, key in enumerate(summaries):
        st.header("summary using "+ key)
        st.write(summaries[key][0]["summary_text"])


    HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""
    st.header("Entities in recording")
    st.write(HTML_WRAPPER.format(displacy_response), unsafe_allow_html=True)