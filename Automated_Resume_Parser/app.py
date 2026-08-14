from flask import Flask, render_template, request
import os
import pdfplumber

from parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education
)

from db import init_db, insert_candidate, search_candidates


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# Initialize database
init_db()


@app.route("/", methods=["GET", "POST"])
def home():


    candidate = None

    if request.method == "POST":

        file = request.files.get("resume")

        if not file or file.filename == "":
            return render_template(
                "index.html",
                error="Please select a PDF resume."
            )

        if not file.filename.lower().endswith(".pdf"):
            return render_template(
                "index.html",
                error="Only PDF files are allowed."
            )

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            file.filename
        )

        file.save(file_path)


        # Extract text from PDF
        with pdfplumber.open(file_path) as pdf:

            text = ""

            for page in pdf.pages:

                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"


        # Extract information
        name = extract_name(text)
        email = extract_email(text)
        phone = extract_phone(text)
        skills = extract_skills(text)
        education = extract_education(text)


        # Store candidate
        insert_candidate(
            name,
            email,
            phone,
            skills,
            education
        )


        candidate = {
            "name": name,
            "email": email,
            "phone": phone,
            "skills": skills,
            "education": education
        }


    return render_template(
        "index.html",
        candidate=candidate
    )

@app.route("/search")
def search():

    keyword = request.args.get("keyword", "").strip()

    candidates = []

    if keyword:
        candidates = search_candidates(keyword)

    return render_template(
        "search.html",
        candidates=candidates,
        keyword=keyword
    )

if __name__ == "__main__":
    app.run(debug=True)