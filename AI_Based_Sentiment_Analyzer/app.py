
from flask import Flask, render_template, request
from transformers import pipeline
import sqlite3

app = Flask(__name__)

sentiment = pipeline("sentiment-analysis")


def init_db():
    connection = sqlite3.connect("sentiment.db")
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        review TEXT,
        sentiment TEXT,
        confidence REAL
    )
    """)

    connection.commit()
    connection.close()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        review = request.form["review"]

        result = sentiment(review)

        label = result[0]["label"]
        score = result[0]["score"]

        connection = sqlite3.connect("sentiment.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO reviews (review, sentiment, confidence) VALUES (?, ?, ?)",
            (review, label, score)
        )

        connection.commit()
        connection.close()

        return render_template(
            "index.html",
            label=label,
            score=score
        )

    return render_template("index.html")

@app.route("/history")
def history():

    connection = sqlite3.connect("sentiment.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM reviews")
    reviews = cursor.fetchall()

    connection.close()

    return render_template("history.html", reviews=reviews)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

