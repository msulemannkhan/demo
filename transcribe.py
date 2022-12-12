import pickle
import whisper
import pandas as pd

MODEL_SIZE = "large"
FILE_NAME = "audio_sample2.mp3"

model = whisper.load_model(MODEL_SIZE)
transcription_response = model.transcribe(FILE_NAME)

transcription_segments = []
for segment in transcription_response["segments"]:
    transcription_segments.append(
        [str(segment["start"]), str(segment["end"]), segment["text"]]
        )

with open("data/transcribed_text.txt", "w") as file:
    pickle.dump(transcription_segments, file)