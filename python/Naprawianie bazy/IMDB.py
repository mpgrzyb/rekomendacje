# -*- coding: UTF-8 -*-
from urllib2 import Request, urlopen, HTTPError
import json
from pprint import pprint
import re


def SearchMovieById(movie_id):
	headers = {"Accept": "application/json"}
	request = Request("http://mymovieapi.com/?id=" + movie_id + "&type=json&plot=simple&episode=1&lang=en-US&aka=simple&release=simple&business=0&tech=0", headers=headers)
	response_body = urlopen(request).read()
	data = json.loads(response_body)
	
	for key in data:
		if key == 'code':
			return None
	return data

def SearchMovieByTitle(title):
	headers = {"Accept": "application/json"}
	request = Request("http://mymovieapi.com/?title=" + title + "&type=json&plot=simple&episode=1&limit=1&yg=0&mt=none&lang=en-US&offset=&aka=simple&release=simple&business=0&tech=0", headers=headers)
	response_body = urlopen(request).read()
	data = json.loads(response_body)

	for key in data:
		if key == 'code':
			return None
	return data

# print SearchMovieByTitle("The godfather")
# data = SearchMovieById("tt1535109")
# print data['directors']