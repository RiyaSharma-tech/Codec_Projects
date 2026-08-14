import re


def extract_name(text):
    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Skip obvious headings
        if line.upper() in [
            "RESUME",
            "CURRICULUM VITAE",
            "CV"
        ]:
            continue

        # If the line contains contact information, stop looking
        if "@" in line or "phone" in line.lower():
            break

        # Candidate name is usually a short line at the beginning
        if len(line.split()) <= 4:
            return line

    return "Not found"


def extract_email(text):
    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'
    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not found"


def extract_phone(text):

    phone_patterns = [
        r'\+\d{1,3}[\s\-]?\d{2,4}[\s\-]?\d{3,4}[\s\-]?\d{3,4}',
        r'\(\d{2,4}\)[\s\-]?\d{3,4}[\s\-]?\d{3,4}',
        r'\b\d{3}[\s\-]\d{3}[\s\-]\d{4}\b',
        r'\b\d{5}[\s\-]\d{5}\b',
        r'\b\d{10}\b'
    ]

    for pattern in phone_patterns:

        match = re.search(pattern, text)

        if match:
            return match.group(0)

    return "Not found"

def extract_skills(text):

    skills_list = [
        "Python",
        "C++",
        "C",
        "HTML",
        "CSS",
        "JavaScript",
        "Flask",
        "MySQL",
        "SQLite",
        "Git",
        "GitHub",
        "Data Structures and Algorithms",
        "Machine Learning",
        "Pandas",
        "NumPy",
        "SQL",
        "Java",
        "React",
        "Django",
        "TensorFlow"
    ]

    found_skills = []

    text_lower = text.lower()

    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills

def extract_education(text):

    lines = text.splitlines()

    education = []

    education_started = False

    section_headers = [
        "experience",
        "work experience",
        "professional experience",
        "employment",
        "skills",
        "projects",
        "certifications",
        "achievements",
        "awards",
        "publications",
        "interests",
        "references"
    ]

    for line in lines:

        line_clean = line.strip()

        if not line_clean:
            continue

        line_lower = line_clean.lower()

        # Detect Education section
        if line_lower in ["education", "educational background"]:
            education_started = True
            continue

        # Stop when another major section starts
        if education_started and line_lower in section_headers:
            break

        # Collect education information
        if education_started:
            education.append(line_clean)

    if education:
        return education

    return ["Not found"]