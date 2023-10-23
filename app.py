import streamlit as st
from transformers import pipeline
from transformers import MarianMTModel, MarianTokenizer

# Inisialisasi model terjemahan
model_name = "Helsinki-NLP/opus-mt-id-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Inisialisasi model analisis sentimen
sentiment_pipe = pipeline('sentiment-analysis')

text = st.text_area('Masukkan teks dalam bahasa Indonesia')

if text:
    # Terjemahkan teks ke bahasa Inggris
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    outputs = model.generate(**inputs)
    translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Analisis sentimen
    sentiment_result = sentiment_pipe(translated_text)

    # Tampilkan hasil
    st.write(f"Hasil Analisis Sentimen: {sentiment_result[0]['label']}")
    st.write(f"Terjemahan ke Bahasa Inggris: {translated_text}")
