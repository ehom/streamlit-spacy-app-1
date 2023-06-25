import streamlit as st
import spacy
import spacy_streamlit

print(f"Using SpaCy {spacy.__version__}...")

models = ["en_core_web_sm", "en_core_web_md"]
default_text = "Sundar Pichai is the CEO of Google."
spacy_streamlit.visualize(models, default_text)


