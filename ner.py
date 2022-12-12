import spacy
import pickle
from spacy import displacy
import spacy_transformers

with open("data/transcribed_table", "rb") as fp:
    transcribed_table = pickle.load(fp)

transcribed_text = ""
for item in transcribed_table:
    transcribed_text += item[2]

nlp = spacy.load("en_core_web_lg")
nlp_sm = spacy.load("en_core_web_sm")

nlp_trf = spacy.load("en_core_web_trf")

doc = nlp_trf(transcribed_text)
displacy_response = displacy.render(doc, style="ent")

with open("data/displacy.txt", "w") as file:
    file.write(displacy_response)