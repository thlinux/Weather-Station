from flask import Response, request
from flask_jwt_extended import jwt_required
from database.models import Movie
from flask_restful import Resource

class MoviesApi(Resource):
	@jwt_required
	def get(self):
		movies = Movie.objects().to_json()
		return Response(movies, mimetype="application/json", status=200)

	@jwt_required
	def post(self):
		body = request.get_json()
		movie = Movie(**body).save()
		id = movie.id
		return {'id': str(id)}, 200

class MovieApi(Resource):
	@jwt_required
	def put(self, id):
		body = request.get_json()
		Movie.objects.get(id=id).update(**body)
		return '', 200

	@jwt_required
	def delete(self, id):
		movie = Movie.objects.get(id=id).delete()
		return '', 200
	@jwt_required
	def get(self, id):
		movie = Movie.objects.get(id=id).to_json()
		return Response(movie, mimetype="application/json", status=200)
