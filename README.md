# 💻 Codec Technologies Internship Projects

This repository contains the projects completed as part of my **Codec Technologies Python Developer Internship**.

The repository includes two Python-based web applications demonstrating practical experience in **Artificial Intelligence, Natural Language Processing, Flask, database management, PDF processing, and web development**.

---

## 📂 Projects

### 1. 📄 Automated Resume Parser

**Status: Completed**

An AI-assisted web application that automatically extracts important candidate information from PDF resumes and stores the extracted data in a searchable SQLite database.

The application extracts:

* 👤 Candidate name
* 📧 Email address
* 📱 Phone number
* 🛠️ Technical skills
* 🎓 Education information

**Technologies:**

* Python
* Flask
* PDFPlumber
* spaCy
* SQLite
* HTML
* CSS

**Features:**

* 📤 PDF resume upload
* 📖 PDF text extraction
* 👤 Candidate information extraction
* 🛠️ Technical skill extraction
* 🎓 Education extraction
* 💾 SQLite database storage
* 🔄 Duplicate candidate prevention
* 🔎 Candidate search
* 🌐 Flask web interface
* ⚠️ Missing information handling

➡️ **[View Automated Resume Parser](Automated_Resume_Parser/)**

---

### 2. 🤖 AI-Based Sentiment Analyzer

**Status: Completed**

An AI-powered web application that analyzes user reviews and classifies their sentiment as **POSITIVE** or **NEGATIVE** using a pre-trained Transformer model from Hugging Face.

The application displays the predicted sentiment and confidence score and stores analyzed reviews in a local SQLite database for viewing through the Review History page.

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
* ⚠️ Empty review validation

**Sentiment Model:**

`distilbert-base-uncased-finetuned-sst-2-english`

The model performs binary sentiment classification:

* POSITIVE
* NEGATIVE

> **Note:** The current model does not provide a separate NEUTRAL class. Neutral-style reviews are therefore classified into either POSITIVE or NEGATIVE.

➡️ **[View AI-Based Sentiment Analyzer](AI_Based_Sentiment_Analyzer/)**

---

## 📊 Project Comparison

| Project | Main Purpose | AI/NLP | Database | Framework |
|---|---|---|---|---|
| Automated Resume Parser | Resume information extraction | spaCy / NLP | SQLite | Flask |
| AI-Based Sentiment Analyzer | Review sentiment classification | Hugging Face Transformers | SQLite | Flask |

---

## 🛠️ Skills & Technologies Demonstrated

Through these projects, I gained practical experience with:

* Python
* Flask
* Natural Language Processing
* Artificial Intelligence
* Hugging Face Transformers
* spaCy
* PDF text extraction
* Regular expressions
* SQLite
* HTML
* CSS
* Jinja templating
* Git
* GitHub
* Project documentation

---

## 📁 Repository Structure

    Codec_Projects/
    │
    ├── Automated_Resume_Parser/
    │   ├── app.py
    │   ├── parser.py
    │   ├── db.py
    │   ├── extract_text.py
    │   ├── search_candidates.py
    │   ├── requirements.txt
    │   ├── README.md
    │   ├── .gitignore
    │   ├── templates/
    │   ├── static/
    │   └── screenshots/
    │
    ├── AI_Based_Sentiment_Analyzer/
    │   ├── app.py
    │   ├── requirements.txt
    │   ├── README.md
    │   ├── .gitignore
    │   ├── templates/
    │   ├── static/
    │   └── screenshots/
    │
    └── README.md

---

## ⚙️ Running the Projects

Each project contains its own `README.md` with detailed installation and usage instructions.

### Automated Resume Parser

    cd Automated_Resume_Parser
    pip install -r requirements.txt
    python -m spacy download en_core_web_sm
    python app.py

Open:

`http://127.0.0.1:5000`

### AI-Based Sentiment Analyzer

    cd AI_Based_Sentiment_Analyzer
    pip install -r requirements.txt
    python app.py

Open:

`http://127.0.0.1:5000`

---

## 🗄️ Database

Both projects currently use **SQLite** as their local database solution.

SQLite was selected because it is lightweight, easy to configure, and suitable for these internship projects.

### Automated Resume Parser

Stores:

* Candidate name
* Email
* Phone number
* Skills
* Education

### AI-Based Sentiment Analyzer

Stores:

* Review ID
* Review text
* Sentiment
* Confidence score

Local database files and generated test data are excluded from the GitHub repository using `.gitignore`.

---

## 🔮 Future Enhancements

Possible future improvements include:

* PostgreSQL integration
* MongoDB integration
* Advanced NLP-based extraction
* Improved resume parsing for different layouts
* DOC/DOCX resume support
* Resume ranking and candidate scoring
* Advanced sentiment classification
* Authentication and user accounts
* Admin dashboards
* CSV/Excel data export
* Cloud deployment

---

## 🎯 Internship Learning Outcomes

These projects provided practical experience in:

* Python application development
* Flask web development
* Artificial Intelligence
* Natural Language Processing
* Machine Learning
* Pre-trained Transformer models
* PDF processing
* Database management
* HTML and CSS
* Git and GitHub
* Project documentation

---

## 🎓 Internship

These projects were developed as part of the **Codec Technologies Python Developer Internship**.

The projects were created to gain practical experience in Python development, Artificial Intelligence, Natural Language Processing, web application development, database management, and GitHub-based project organization.

---

## 👩‍💻 Author

**Riya Sharma**

B.Tech Computer Science Engineering Student

**Codec Technologies Python Developer Internship – 2026**
