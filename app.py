from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

data = []


@app.route("/")
def index():
    return render_template("index.html", books=data)


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form.get("title")
    cover_url = request.form.get("cover_url")
    if title and cover_url:
        data.append({"title": title, "cover_url": cover_url})
    return redirect(url_for("index"))


@app.route("/random")
def random_books():
    if len(data) >= 5:
        selected_books = random.sample(data, 5)
    else:
        selected_books = data
    return render_template("random.html", books=selected_books)
