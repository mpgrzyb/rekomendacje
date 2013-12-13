# -*- coding: UTF-8 -*-
from urllib2 import Request, urlopen, HTTPError
import json
import time
from pprint import pprint

def change_time(czas):
  hours = int(czas) / 60
  minutes = int(czas) - hours * 60
  if hours > 0:
      hours = str(hours) + ' godz. '
  else:
      hours = ''
  return hours + str(minutes) + ' min.'

def FindMovie(title, date):
	headers = {"Accept": "application/json"}
	try:
		_title = str(title)
		title = title.replace(' ', '+')
		title = title.replace('.', '+')
	except UnicodeEncodeError, e:
		return None

	try:
		request = Request("http://private-ba33-themoviedb.apiary.io/3/search/movie?api_key=70d907e0f58362eee8ad8f72503d4dc2&query=" + title.strip(), headers=headers)
	except:
		return '404'	
	try:
		response_body = urlopen(request).read()
	except:
		print '!!!!!  BŁĄD  !!!!!'
		time.sleep(10)
		response_body = urlopen(request).read()
		pass

	response_body = response_body.replace('-nan','0')
	response_body = response_body.replace('nan','0')
	data = json.loads(response_body)
	
	movies_count =  len(data['results'])
	if movies_count == 0:
		return None

	movie_id = None

	for x in range(0, len(data['results'])):
		tmdb_title = data['results'][x]['title']
		tmdb_release_year = data['results'][x]['release_date'][0:4]
		if tmdb_release_year == date:
			movie_id = data['results'][x]['id']
			return str(movie_id)

	return movie_id

def GetAllData(movieId):
	headers = {"Accept": "application/json"}
	try:
		request = Request("http://private-ba33-themoviedb.apiary.io/3/movie/" + str(movieId) + "?api_key=70d907e0f58362eee8ad8f72503d4dc2", headers=headers)
	except ValueError:
		return '404'	
	try:
		response_body = urlopen(request).read()
	except:
		print '!!!!!  BŁĄD  !!!!!'
		time.sleep(10)
		response_body = urlopen(request).read()
		pass
	data = json.loads(response_body)
	return data

def GetAllData_cast(movieId):
	headers = {"Accept": "application/json"}
	request = Request("http://private-ba33-themoviedb.apiary.io/3/movie/" + str(movieId) + "/casts?api_key=70d907e0f58362eee8ad8f72503d4dc2", headers=headers)
	try:
		response_body = urlopen(request).read()
	except:
		print '!!!!!  BŁĄD  !!!!!'
		time.sleep(10)
		response_body = urlopen(request).read()
		pass
	data = json.loads(response_body)
	return data

def GetAllData_photo(movieId):
	headers = {"Accept": "application/json"}
	request = Request("http://private-ba33-themoviedb.apiary.io/3/movie/" + str(movieId) + "/images?api_key=70d907e0f58362eee8ad8f72503d4dc2", headers=headers)
	data = None
	try:
		try:
			print '1'
			response_body = urlopen(request).read()
			data = json.loads(response_body)
		except HTTPError, e:  # Python 2.5 syntax
			return None
			if e.code == 404 or e.code == 504:
				print '2'
				e.msg = 'data not found on remote: %s' % e.msg
			raise
	except HTTPError, e:
		return None
		print e

	return data

def GetVoteAverage(data):
	vote_average = data['vote_average']
	return vote_average

def GetPoster(data):
	posters = data['posters']
	for poster in posters:
		aspect_ratio = poster['aspect_ratio']
		if (aspect_ratio == 0.67) and poster['file_path']!='':
			return 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/w780' + poster['file_path']
	return None

def GetReleaseDate(data):
	release_date = data['release_date'].strip()
	if release_date != None and release_date!='':
		return release_date
	else:
		return '2000-01-01'

def GetGenres(data):
	genres_list = []
	for genre in data['genres']:
		genre_name = str(genre['name'])
		if genre_name in GenresList:
			id_genre = GenresList.index(genre_name) + 1
			genre = GenresList[id_genre]
			genres_list.append(genre)
	return genres_list

def GetRuntime(data):
	runtime = data['runtime']
	if runtime != None:
		return change_time(runtime)
	else:
		return '0 min.'

def GetTagline(data):
	tagline = data['tagline']
	return tagline

def GetPopularity(data):
	popularity = data['popularity']
	return popularity

def GetDescription(data):
	overview = data['overview']
	return overview

def GetProductionCountries(data):
	data = data['production_countries']
	countries = []
	for country in data:
		countries.append(country['name'])
	return countries

def GetPhoto(data):
	photos = data['backdrops']
	for photo in photos:
		aspect_ratio = photo['aspect_ratio']
		if aspect_ratio == 1.78 and photo['file_path']!='':
			return 'http://d3gtl9l2a4fn1j.cloudfront.net/t/p/w780' + photo['file_path']
	return None

def GetCast(data):
	full_cast = data['cast']
	cast = []
	count = 0
	for roles in full_cast:
		count = count + 1
		role = []
		role.append(roles['name'])
		role.append(roles['character'])
		cast.append(role)
		if count == 5:
			break
	return cast

def GetDirector(data):
	full_crew = data['crew']
	cast = []
	count = 0
	for people in full_crew:
		role = people['job']
		if role == 'Director':
			director = people['name'].encode('utf8', 'ignore')
			return director
	return None

def GetKeywords(movieId):
	# from urllib2 import Request, urlopen
	headers = {"Accept": "application/json"}
	request = Request("http://private-ba33-themoviedb.apiary.io/3/movie/" + str(movieId) + "/keywords?api_key=70d907e0f58362eee8ad8f72503d4dc2", headers=headers)
	
	try:
		response_body = urlopen(request).read()
	except:
		print '!!!!!  BŁĄD  !!!!!'
		time.sleep(10)
		response_body = urlopen(request).read()
		pass
		

	data = json.loads(response_body)
	keywords_data = data['keywords']
	keywords = []
	for keyword in keywords_data:
		keywords.append(keyword['name'].strip())
	return keywords

def GetIMDBId(data):
	id = data['imdb_id']
	return id

# print FindMovie("Scary MoVie" , "2013")