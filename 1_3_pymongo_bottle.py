# -*- coding: utf-8 -*-

import bottle, pymongo

def getMovies():
	connection = pymongo.MongoClient('localhost', 27017)
	dbVideo = connection.video

	movies = dbVideo.movies.find({})
	output = "<h1>Movies</h1><ul>"
	if movies:
		for index, movie in enumerate(movies):
			output += "<h3>Movie " + str(index) + ":</h3><li>Title: " + movie['title'] + "</li>" + \
				"<li>Year: " + '{0:g}'.format(movie['year']) + "</li>"
	output += "</ul>"
	return output

@bottle.route('/')
def index():
	return getMovies()

if __name__ == '__main__':
	bottle.run(host='localhost', port=8082, debug=True, reloader=True)