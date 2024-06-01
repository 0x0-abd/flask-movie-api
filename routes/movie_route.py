from flask import Blueprint
from controllers.movie_controller import fetch_name, fetch_by_genre, fetch_popular, fetch_by_id
from flask_cors import cross_origin

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/search/<search_keyword>', methods=['GET'])
@cross_origin()
def fetch_data_route(search_keyword):
    return fetch_name(search_keyword)

@movie_bp.route('/search/id/<search_keyword>', methods=['GET'])
@cross_origin()
def fetch_by_id_route(search_keyword):
    return fetch_by_id(search_keyword)

@movie_bp.route('/genre/', methods=['POST'])
@cross_origin()
def fetch_by_genre_route():
    return fetch_by_genre()

@movie_bp.route('/search/', methods=["GET"])
@cross_origin()
def fetch_popular_route():
    return fetch_popular()