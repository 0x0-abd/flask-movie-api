from flask import Flask, jsonify
import requests
from dotenv import load_dotenv
import os
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
load_dotenv()

base_url = os.getenv('BASE_URL')
api_access_token = os.getenv('API_KEY')
production = os.getenv('PRODUCTION', 'False').lower() == 'true'

session = requests.Session()
session.headers.update({
    'accept': 'application/json',
    'Authorization': f'Bearer {api_access_token}'
})

from routes.movie_route import movie_bp
app.register_blueprint(movie_bp, url_prefix='')

@app.route("/")
def home():
    return "Hello World!!!!"


if __name__ == "__main__":
    app.run(debug=not production)