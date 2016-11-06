# -*- coding: utf-8 -*-

import sys
import pprint
import pymongo

def main():
	connection = pymongo.MongoClient("localhost", 27017)
	database = connection.video
	collection = database.movieDetails

	# En MongoDB projection se refiere a seleccionar ciertos campos de los documentos que
	# se quieren buscar para que no recibamos todos los campos de todos los documentos.
	# En bases de datos relacionales equivale a escribir columnas en el SELECT.


	movies = collection.find({"year": 1952}, {"title": 1, "runtime": 1, "_id": 0})
	# Si queremos obtener un campo del documento, se indica con un 1 seguido del nombre del campo.
	# Si no queremos obtener un campo del documento, se indica con un 0 seguido del nombre del campo.
	# El _id siempre se devuelve al usar el método find, por eso, lo hemos excluido usando "_id": 0

	print("#" * 75 + " PROJECTION " + "#" * 75)

	if movies:
		for movie in movies:
			print(movie)

	print("\n"+ "/" * 140 + "\n")

	movies = collection.find({"year": 1952}, {"awards": 0}) # Queremos todos los campos menos el campo awards
	pp = pprint.PrettyPrinter(indent=4)
	if movies:
		for movie in movies:
			pp.pprint(movie)

if __name__ == "__main__":
	main()