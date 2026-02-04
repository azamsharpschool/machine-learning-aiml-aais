
#  flask --app main --debug run 

from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

movies = [
            {"id": 1, "title": "Inception", "year": 2010, "genre": "Sci-Fi"},
            {"id": 2, "title": "The Dark Knight", "year": 2008, "genre": "Action"},
            {"id": 3, "title": "Interstellar", "year": 2014, "genre": "Sci-Fi"},
            {"id": 4, "title": "The Matrix", "year": 1999, "genre": "Sci-Fi"},
            {"id": 5, "title": "Gladiator", "year": 2000, "genre": "Action"},
            {"id": 6, "title": "The Shawshank Redemption", "year": 1994, "genre": "Drama"},
            {"id": 7, "title": "The Godfather", "year": 1972, "genre": "Drama"},
            {"id": 8, "title": "Forrest Gump", "year": 1994, "genre": "Drama"},
            {"id": 9, "title": "Mad Max: Fury Road", "year": 2015, "genre": "Action"},
            {"id": 10, "title": "Avengers: Endgame", "year": 2019, "genre": "Action"}
        ]

@app.route("/")
def index():
    
    sort_order = request.args.get("sort", "asc")

    # Work on a *copy* of the global list, and give it a new name
    sorted_list = sorted(
        movies,
        key=lambda m: m["title"],
        reverse=(sort_order == "desc")
    )

    return render_template("index.html", movies=sorted_list, sort_order=sort_order)

@app.route("/add-movie", methods=["POST"])
def add_movie(): 
    title = request.form.get("title")
    genre = request.form.get("genre") 
    year = request.form.get("year")

    movie = {
        "title": title, 
        "genre": genre, 
        "year": year
    }

    movies.append(movie)
    return redirect(url_for("index"))

@app.route("/hello")
def hello(): 
    return "<h1>Hello</h1>"

@app.route("/api/movies")
def all_movies():
    return jsonify(movies)

@app.route("/api/movies/genre/<genre>")
def movies_by_genre(genre):
    # Filter
    filtered = [m for m in movies if m["genre"].lower() == genre.lower()]
    return jsonify(filtered)
