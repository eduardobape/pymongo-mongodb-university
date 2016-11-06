# -*- coding:utf-8 -*-

import pymongo

def main():
	try:
		# connection to the database
		connection = pymongo.MongoClient('localhost', 27017)
		videoDB = connection.video

		# get the collection
		moviesCol = videoDB.movies

		output = ""
		movies = moviesCol.find()
		
		if movies:
			for movie in movies:
				output += "Title: " + movie['title'] + " Year: " + str(movie['year']) + "\n"

		return output
	except Exception as e:
		print e
		

if __name__ == '__main__':
	print main()