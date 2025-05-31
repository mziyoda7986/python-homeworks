import requests
import random

key = '8dc288049d40ada1417b5b800078e6a4'
def get_genres():
    url = f'https://api.themoviedb.org/3/genre/movie/list'
    params = {
        'api_key': key,
        'laguage': 'en-US'
    }
    response = requests.get(url, params=params)
    genres = response.json()['genres']
    return {genre['name'].lower(): genre['id'] for genre in genres}

def get_movies_by_genre(genre_id):
    url = f'https://api.themoviedb.org/3/discover/movie'
    params = {
        'api_key': key,
        'with_genres': genre_id,
        'sort_by': 'popularity.desc',
        'page': random.randint(1, 5)  # random page for variety
    }
    response = requests.get(url, params=params)
    return response.json().get('results', [])

def recomend_movie():
    genres = get_genres()
    print("Available genres:", ', '.join(genres.keys()))
    user = input("Enter a movie genre:").lower()

    if user not in genres:
        print("Genre not found!")
        return
    
    genre_id = genres[user]
    movies = get_movies_by_genre(genre_id)

    if not movies:
        print("No movies found for this genre.")
        return
    
    movie = random.choice(movies)
    print(f"Recommended Movie: {movie['title']}")
    print(f"Overview: {movie.get('overview', 'No overview available.')}")
    print(f"Release Date: {movie.get('release_date', 'N/A')}")
    print(f"Rating: {movie.get('vote_average', 'N/A')} / 10")

recomend_movie()