# -*- coding: utf-8 -*-

import pymongo

def main():
	connection = pymongo.MongoClient('localhost', 27017)
	db = connection.video
	collection = db.movies

	# Inserto una película
	try:
		print "Insertando la película Minority Report"
		collection.insert_one({'title': 'Minority Report', 'year': 2008, 'imdb': 'tt384739489'})
	except Exception as e:
		print 'Error al insertar, ', e

	try:
		print "Insertando una película con el mismo id de otra ya existente en la colección"
		# Voy a intentar insertar otra película diferente pero con el mismo id que la anterior
		# Se producirá un error al intentar duplicar un id ya existente en otro documento
		movie = collection.find({'title': 'Minority Report'}).next()
		if movie:
			collection.insert_one({'_id': movie['_id'], 'title': 'Pokemon', 'year': 1996, 'imdb': 'tt3434324324'})
	except Exception as e:
		print 'Error al insertar con id duplicado, ', e


if __name__ == '__main__':
	main()