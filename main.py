from flask import Flask, jsonify, request
import csv 

all_movies = []

with open('movies.csv', encoding = "utf-8") as f:
    reader = csv.reader(f)
    data = list(reader)

    all_movies = data[1:]

liked_movies = []
disliked_movies = []
dnw_movies = []
#dnw -> did not watch

app = Flask(__name__)

@app.route('/get-movie')

def get_movie():
    return jsonify({
        'data': all_movies[0],
        'status': "success"
    })

@app.route('/liked-movies', methods = ["POST"])

def like_movie():
    global all_movies

    movie = all_movies[0]
    all_movies = all_movies[1:]

    liked_movies.append(movie)
    return jsonify({'status': "success"}), 201

@app.route('/disliked-movies', methods = ["POST"])

def dislike_movie():
    global all_movies

    movie = all_movies[0]
    all_movies = all_movies[1:]

    disliked_movies.append(movie)
    return jsonify({'status': "success"}), 201

@app.route('/dnw-movies', methods = ["POST"])

def dnw_movie():
    global all_movies
    
    movie = all_movies[0]
    all_movies = all_movies[1:]

    dnw_movies.append(movie)
    return jsonify({'status': "success"}), 201

if __name__ == "__main__":
    app.run()
