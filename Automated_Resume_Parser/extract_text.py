import pdfplumber

from parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
    extract_education
)

from db import init_db, insert_candidate


pdf_path = "resumes/sample_resume.pdf"


# Initialize database
init_db()


# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"


# Extract candidate information
name = extract_name(text)
email = extract_email(text)
phone = extract_phone(text)
skills = extract_skills(text)
education = extract_education(text)


# Store candidate in database
insert_candidate(
    name,
    email,
    phone,
    skills,
    education
)


# Display extracted information
print("========== EXTRACTED INFORMATION ==========")

print("Name:", name)
print("Email:", email)
print("Phone:", phone)

print("Skills:", ", ".join(skills))

print("Education:")

for item in education:
    print(" -", item)

print("===========================================")

print("Candidate saved to database successfully!")