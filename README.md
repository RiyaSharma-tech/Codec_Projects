# Codec Technologies Internship Projects

This repository contains the projects completed as part of my **Codec Technologies Internship**.

## 📂 Projects

### 1. AI-Based Resume Parser

**Status:** Pending

A web-based resume parsing application that extracts relevant information from resumes and presents it in a structured format.

**Technologies:**

* Python
* Flask
* PostgreSQL
* Resume parsing libraries

[View Resume Parser Project](./Resume_Parser)

---

### 2. AI-Based Sentiment Analyzer

**Status:** Completed

An AI-powered web application that analyzes user reviews and classifies their sentiment as **POSITIVE** or **NEGATIVE** using a pre-trained Transformer model from Hugging Face.

The application also stores analyzed reviews in a local SQLite database and provides a review history page.

**Technologies:**

* Python
* Flask
* Hugging Face Transformers
* PyTorch
* SQLite
* HTML
* CSS

**Features:**

* 🤖 AI-based sentiment analysis
* 🟢 Positive sentiment detection
* 🔴 Negative sentiment detection
* 📊 Confidence score
* 💾 Review storage using SQLite
* 📜 Review history
* 🌐 Flask web interface
* 🎨 User-friendly interface

**Sentiment Model:**

`distilbert-base-uncased-finetuned-sst-2-english`

The current model performs binary sentiment classification:

* POSITIVE
* NEGATIVE

> Note: The model does not have a separate NEUTRAL class. Neutral-style reviews are therefore classified into either POSITIVE or NEGATIVE.

[View Sentiment Analyzer Project](./AI_Based_Sentiment_Analyzer)

---

## 🛠️ Repository Structure

```text
codec_projects/
│
├── Task_1-Resume-Parser/
│   ├── app.py
│   ├── requirements.txt
│   ├── README.md
│   └── ...
│
└── AI_Based_Sentiment_Analyzer/
    ├── app.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── templates/
    ├── static/
    └── screenshots/
```

## 🎯 Internship

These projects were developed as part of the **Codec Technologies Internship**, with the aim of gaining practical experience in:

* Python development
* Web application development
* Artificial Intelligence and Machine Learning
* Natural Language Processing
* Database management
* Flask
* GitHub and project documentation

---

## 👩‍💻 Author

**Riya Sharma**
