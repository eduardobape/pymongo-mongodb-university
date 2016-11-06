# -*- coding: utf-8 -*-

import sys
from pprint import pprint
import pymongo

def main(databaseName, collectionName):
	try:
		connection = pymongo.MongoClient('localhost', 27017)
		database = connection[str(databaseName)]
		collection = database[str(collectionName)]
		# Borramos todos los documentos de la colección para que el siguiente insert_many no produzca
		# ningún error en caso de que alguna película ya existiera en la colección
		collection.delete_many({})

		movies = [
			{"_id": "001", "title": "Jaws", "year": 1983, "imdb": "td123456"},
			{"_id": "002", "title": "Saw", "year": 2000, "imdb": "td123457"}
		]

		collection.insert_many(movies)

		print("Colección ANTES")
		for movie in collection.find({}):
			pprint(movie)
		
		# Inserting new documents, but one of them has the same _id than a previous one
		movies = [
			{"_id": "003", "title": "Minority Report", "year": 2008, "imdb": "td123458"},
			{"_id": "002", "title": "Saw II", "year": 2008, "imdb": "td123459"},
			{"_id": "004", "title": "Jurasic Park", "year": 1996, "imdb": "td123460"},
			{"_id": "005", "title": "Jurasic Park II", "year": 1998, "imdb": "td123461"}
		]
		# Al usar ordered=True, la película con id=003 se insertará, la película con id=002 no se insertará porque ya
		# hay otra película en la colección con el mismo _id. Se producirá un error, pero éste no impide que se inserte
		# la película con id=004
		collection.insert_many(movies, ordered=False)
		
	except pymongo.errors.BulkWriteError as bwe:
		pprint(bwe.details)
		print("Colección DESPUÉS")
		for movie in collection.find({}):
			pprint(movie)

if __name__ == '__main__':
	# Pass the database name as a Python command line argument
	if len(sys.argv) >= 3:
		# The first command line argument is the python script filename
		# The second command line argument is the collection name
		# The third command line argument is the database name
		main(sys.argv[1], sys.argv[2])