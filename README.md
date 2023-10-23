# Translator ID to EN (Huggingface Space)

---
title: Translator ID to EN
emoji: 😻
colorFrom: green
colorTo: pink
sdk: streamlit
sdk_version: 1.27.2
app_file: app.py
pinned: false
---

Program ada di sini: https://huggingface.co/spaces/mabzak/translator-id-to-en

## Kenapa saya buat program ini?
Ini adalah program pertama saya di huggingface (HF), jadi tolong maklumi jika banyak kesalahan.

Alakisah saya ingin membuat program AI pembuat gambar tapi inputnya bahasa indonesia, masalahnya saya kesulitan membuat penerjemah di huggingface karna paket translation google gk berfungsi, 

Jadi saya harus mencari dahulu model yang dapat menerjemahkan bahasa dan saya menemukan model
[Helsinki-NLP/opus-mt-id-en](https://huggingface.co/Helsinki-NLP/opus-mt-id-en)

Pertama saya membuat input normal yang akan menampilkan output, sumber dari [youtube](https://www.youtube.com/watch?v=3bSVKNKb_PY&ab_channel=HuggingFace)
lalu saya menambahkan fungsi mol [opus](https://huggingface.co/Helsinki-NLP/opus-mt-id-en) kedalamnya dan jadilah progam ini

Program ini diharap bisa menjadi dasar penerjemahan untuk membuat input-input dengan bahasa indonesia untuk program AI lainnya

## Standar Code

Paket:
```
sentencepiece
transformers
torch
```

Code Instalisasi:
```
from transformers import MarianMTModel, MarianTokenizer

# Inisialisasi model terjemahan
model_name = "Helsinki-NLP/opus-mt-id-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
```

Code Penggunaan:
```
# Terjemahkan teks ke bahasa Inggris
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
outputs = model.generate(**inputs)
translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
```
