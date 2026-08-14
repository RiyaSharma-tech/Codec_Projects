import sqlite3


DATABASE = "resume_parser.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            phone TEXT,
            skills TEXT,
            education TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_candidate(name, email, phone, skills, education):
    connection = get_connection()
    cursor = connection.cursor()

    skills_text = ", ".join(skills)
    education_text = ", ".join(education)

    # Check if candidate already exists
    cursor.execute(
        "SELECT id FROM candidates WHERE email = ?",
        (email,)
    )

    existing_candidate = cursor.fetchone()

    if existing_candidate:

        cursor.execute(
            """
            UPDATE candidates
            SET name = ?,
                phone = ?,
                skills = ?,
                education = ?
            WHERE email = ?
            """,
            (
                name,
                phone,
                skills_text,
                education_text,
                email
            )
        )

        print("Existing candidate updated.")

    else:

        cursor.execute(
            """
            INSERT INTO candidates
            (name, email, phone, skills, education)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                name,
                email,
                phone,
                skills_text,
                education_text
            )
        )

        print("New candidate inserted.")

    connection.commit()
    connection.close()

def search_candidates(keyword):
    connection = get_connection()
    cursor = connection.cursor()

    search_term = f"%{keyword}%"

    cursor.execute(
        """
        SELECT * FROM candidates
        WHERE name LIKE ?
           OR email LIKE ?
           OR phone LIKE ?
           OR skills LIKE ?
           OR education LIKE ?
        """,
        (
            search_term,
            search_term,
            search_term,
            search_term,
            search_term
        )
    )

    candidates = cursor.fetchall()

    connection.close()

    return candidates