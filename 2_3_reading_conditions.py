# -*- coding: utf-8 -*-

import sys
import datetime
import pprint
import pymongo

def main():
	try:
		connection = pymongo.MongoClient("localhost", 27017)
		database = connection.video
		collection = database.movies

		collection.drop()

		myMovies = [
			{
				"title" : "Toy Story 2",
			    "year" : 2000,
			    "rated" : "B",
			    "released" : datetime.datetime(2010, 06, 18, 04, 0, 0),
			    "runtime" : 103,
			    "imdb": "tt0435761",
			    "countries" : [
			        "USA"
			    ],
			    "genres" : [
			        "Animation",
			        "Adventure",
			        "Comedy"
			    ],
			    "director" : "Lee Unkrich",
			    "writers" : [
			        "John Lasseter",
			        "Andrew Stanton",
			        "Lee Unkrich",
			        "Michael Arndt"
			    ],
			    "awards" : {
			        "oscars" : [
			            {"bestAnimatedFeature": "won"},
			            {"bestMusic": "won"},
			            {"bestPicture": "nominated"},
			            {"bestSoundEditing": "nominated"},
			            {"bestScreenplay": "nominated"}
			        ],
			        "wins" : 56,
			        "nominations" : 86,
			        "text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
			    },
			    "ratings": {
			    	"rotten-tomatoes": 9,
			    	"metacritic": 10,
			    	"imdb": 9.4
			    }
			},
			{
				"title" : "Jurassic Park",
			    "year" : 1996,
			    "rated" : "B",
			    "released" : datetime.datetime(1998, 06, 20, 04, 0, 0),
			    "runtime" : 120,
			    "imdb": "tt0435762",
			    "countries" : [
			        "USA"
			    ],
			    "genres" : [
			        "Adventure",
			    ],
			    "director" : "Steven Spielberg",
			    "writers" : [
			        "Mariano Ozores",
			        "Paco Ozores",
			        "Mariano González"
			    ],
			    "awards" : {
			        "oscars" : [
			            {"bestAnimatedFeature": "won"},
			            {"bestMusic": "won"},
			            {"bestPicture": "nominated"},
			            {"bestSoundEditing": "nominated"},
			            {"bestScreenplay": "nominated"}
			        ],
			        "wins" : 100,
			        "nominations" : 90,
			        "text" : "Won 2 Oscars. Another 56 wins & 86 nominations."
			    },
			    "ratings": {
			    	"rotten-tomatoes": 10,
			    	"metacritic": 10,
			    	"imdb": 10
			    }
			},
			{
				"title" : "Minority Report",
			    "year" : 2000,
			    "rated" : "B",
			    "released" : datetime.datetime(2010, 06, 26, 06, 0, 0),
			    "runtime" : 120,
			    "imdb": "tt0435763",
			    "countries" : [
			        "USA",
			        "Canada"
			    ],
			    "genres" : [
			        "Science fiction",
			    ],
			    "director" : "Barry Wilson",
			    "writers" : [
			        "Paco paquito Paco",
			        "Paco Ozores"
			    ],
			    "awards" : {
			        "oscars" : [
			            {"bestAnimatedFeature": "won"},
			            {"bestMusic": "nominated"},
			            {"bestPicture": "nominated"},
			            {"bestSoundEditing": "nominated"},
			            {"bestScreenplay": "nominated"}
			        ],
			        "wins" : 26,
			        "nominations" : 34,
			        "text" : "Won 1 Oscars. Another 56 wins & 86 nominations."
			    },
			    "ratings": {
			    	"rotten-tomatoes": 8.5,
			    	"metacritic": 8,
			    	"imdb": 8.2
			    }
			}
		]

		collection.insert_many(myMovies)

		print("BÚSQUEDA BASADA EN CONDICIONES DE 2 PROPIEDADES DE UN DOCUMENTO")
		print("Películas lanzadas en el año 2000 y con rated=B")
		# Hacemos una búsqueda basada en condiciones de 2 propiedades
		cursor = collection.find({"year": 2000, "rated": "B"})
		pp = pprint.PrettyPrinter(indent=4)

		for movie in cursor:
			pp.pprint(movie)

		print("BÚSQUEDA EN DOCUMENTOS ANIDADOS DENTRO DE UN DOCUMENTO")
		print("Películas que hayan sido nominadas 34 veces en diferentes premios")
		# Buscamos películas basándonos en condiciones dentro de documentos anidados
		# Buscamos las peículas que hayan sido nominadas 34 veces
		cursor = collection.find({"awards.nominations": 34})
		pp = pprint.PrettyPrinter(indent=4)

		for movie in cursor:
			pp.pprint(movie)

		print("BÚSQUEDA EN ARRAYS DENTRO DE UN DOCUMENTO - CUALQUIER VALOR CONTENIDO EN EL ARRAY")
		print("Películas que tengan como escritores a Paco Ozores")
		# Búsqueda en arrays con un valor que esté dentro del array
		# Buscamos las películas que tengan como escritores a "Paco Ozores"
		cursor = collection.find({"writers": "Paco Ozores"})
		pp = pprint.PrettyPrinter(indent=4)

		for movie in cursor:
			pp.pprint(movie)

		print("BÚSQUEDA EN DOCUMENTOS ANIDADOS DENTRO DE UN DOCUMENTO \
			- VALORES EXACTOS CONTENIDOS EN EL ARRAY EN EL ORDEN INDICADO")
		print("Películas que hayan sido escritas sólo por 'Paco paquito Paco' y 'Paco Ozores', \
			y que dichos escritores figuren en este orden en el array")
		# Búsqueda en arrays que contengan sólo los elementos que queremos y ninguno más, y en el orden que le indiquemos
		# Buscamos las películas que tengan como escritores SÓLO a "Paco paquito Paco" y "Paco Ozores", en este orden.
		cursor = collection.find({"writers": ["Paco paquito Paco", "Paco Ozores"]})
		# Si una películas tiene como valor writers:["Paco Ozores", "Paco paquito Paco"], este película no coincide con
		# la búsqueda anterior, ya que el orden de los escritores no es el mismo que el buscado
		pp = pprint.PrettyPrinter(indent=4)

		for movie in cursor:
			pp.pprint(movie)


	except Exception as e:
		print(e)

if __name__ == "__main__":
	main()