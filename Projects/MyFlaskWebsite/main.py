from flask import Flask, render_template, request

app = Flask(__name__)

movie_name = "Spiderman"

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
    #return render_template("index.html", movie="Lord of the Rings", year=2001)
    return render_template("index.html", all_movies=movies)

@app.route("/add-movie", methods=["POST", "GET"])
def add_movie(): 

    if request.method == "POST": 
        title = request.form.get("movie_name")
        year = request.form.get("movie_year")
        genre = request.form.get("movie_genre")

        movie = { id: len(movies) + 1, "title": title, "year": year, "genre": genre }
        movies.append(movie)
        return render_template("index.html", all_movies=movies)

    return render_template("add_movie.html")

# /127.0.0.1:5000/genre/action 
# /127.0.0.1:5000/genre/kids 
# /127.0.0.1:5000/genre/Horror
@app.route("/genre/<genre_name>")
def movies_by_genre(genre_name): 
    # filter movies based on the genre name 
    filtered_movies = [m for m in movies if m["genre"].lower() == genre_name.lower()]
    return render_template("index.html", all_movies=filtered_movies)


@app.route("/hello")
def greeting(): 
    return "Hi John!"

@app.route("/good-night")
def farewell(): 
    return "<h1>Good night</h1>"

@app.route("/movie")
def movie(): 
    return movie_name 

