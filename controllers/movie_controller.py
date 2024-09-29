import requests
from flask import jsonify, request
import os

# Get environment variables
base_url = os.getenv('BASE_URL')
api_access_token = os.getenv('API_KEY')

# Create a session object
session = requests.Session()
session.headers.update({
    'accept': 'application/json',
    'Authorization': f'Bearer {api_access_token}'
})

def fetch_name(search_keyword):
    try:
        response = session.get(f'{base_url}/search/movie?query={search_keyword}')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return jsonify(data), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

def fetch_popular():
    try:
        response = session.get(f'{base_url}/movie/popular')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return jsonify(data), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

def fetch_by_id(movie_id):
    try:
        response = session.get(f'{base_url}/movie/{movie_id}')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return jsonify(data), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    
def fetch_videos(movie_id):
    try:
        response = session.get(f'{base_url}/movie/{movie_id}/videos')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        trailers = [video for video in data.get('results', []) if video.get('type') == "Trailer"]
        
        return jsonify(trailers), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500

def fetch_by_genre():
    try:
        genres_list = request.json.get('genres')
        if not genres_list:
            return jsonify({'error': 'Genres list is required'}), 400

        # Convert the list to a comma-separated string
        search_keyword = '|'.join(map(str, genres_list))
        print(search_keyword)
        response = session.get(f'{base_url}/discover/movie?with_genres={search_keyword}')
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        return jsonify(data), 200
    except requests.RequestException as e:
        return jsonify({'error': str(e)}), 500
    