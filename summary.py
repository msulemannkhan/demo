import pickle
from transformers import pipeline

with open("data/transcribed_table", "rb") as file:
    transcription_segments = pickle.load(file)

summaries = {}
transcribed_text = ""
for item in transcription_segments:
    transcribed_text += item[2]


summarizer = pipeline("summarization", model="knkarthick/MEETING_SUMMARY")
summaries["knkarthick/MEETING_SUMMARY"] = summarizer(transcribed_text)

summarizer =  pipeline("summarization", model="tanviraumi/meeting-minute")
summaries["tanviraumi/meeting-minute"] = summarizer(transcribed_text)

summarizer = pipeline("summarization")
summaries["summarization"] = summarizer(transcribed_text)

with open("data/summaries.json", "w") as fp:
    pickle.dump(summaries, fp)