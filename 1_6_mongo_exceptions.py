# -*- coding: utf-8 -*-

import pymongo

def main():
	connection = pymongo.MongoClient('localhost', 27017)
	videoDB = connection.video
	movies = videoDB.movies
	movie = {'title': 'Superman II', 'year': 1986, 'imdb': 'tt008765577'}

	print "First insert of de document: ", movie

	try:
		movies.insert_one(movie)
		print "First insert ok"
	except Exception as e:
		print "Insert failed: ", e

	print "Inserting again (second attempt) of the document ", movie

	try:
		movies.insert_one(movie)
		print "Second insert ok"
	except Exception as e:
		print "Second insert failed: ", e

	# Si queremos que no se produzca una excepción al guardar el mismo documento una segunda vez,
	# hay que volver a inicializar la variable movie con el mismo valor una segunda vez
	movie = {'title': 'Superman II', 'year': 1986, 'imdb': 'tt008765577'}
	print "Inserting again (third attempt) of the document ", movie
	try:
		movies.insert_one(movie)
		print "Third insert ok"
	except Exception as e:
		print "Third insert failed ", e

if __name__ == '__main__':
	main()