# -*- coding: UTF-8 -*-
import MySQLdb
import login
import re
import IMDB
import theMovieDB
import datetime
import DoM

def main():
	db = MySQLdb.connect(host=login.GetHost(), user=login.GetUser(), passwd=login.GetPassword(), db=login.GetDataBase(), charset = "utf8", use_unicode = True)
	cur = db.cursor()
	cur_1 = db.cursor()
	cur.execute("select id_pozycja, tytul_org, YEAR(rok_produkcji) from Pozycja where id_pozycja > 577 order by id_pozycja limit 0,50;")
	

	czas_rozpoczecia = datetime.datetime.now()
	count = 0
	removed_movies = 0
	for row in cur:
		count = count + 1
		print "Id filmu: " + str(row[0]) + "  |  " + str(count) + " z 50"

		id_movie = row[0]
		id_movie = str(id_movie)
		title = row[1]
		release_year = str(row[2])

		theMovieDB_id = theMovieDB.FindMovie(title, release_year)

		if theMovieDB_id != None:
			theMovieDB_data = theMovieDB.GetAllData(theMovieDB_id)
			IMDB_id = theMovieDB.GetIMDBId(theMovieDB_data)
			IMDB_data = IMDB.SearchMovieById(IMDB_id)

			if IMDB_data != None:
				director = IMDB_data['directors'][0]
				director = re.escape(director)
				addDirector(cur_1, director, id_movie)

				if 'country' in IMDB_data:
					countries = IMDB_data['country']
					addCountries(cur_1, countries, id_movie)

				rating = IMDB_data['rating']
				runtime = '100'
				if 'rintime' in IMDB_data:
					runtime = IMDB_data['runtime'][0]
					runtime = runtime[:runtime.find(' ')].strip()
				ratingCount = IMDB_data['rating_count']
				rated = ''
				if ('rated' in IMDB_data):
					rated = IMDB_data['rated']
				updateMovie(cur_1, str(rating), runtime, str(ratingCount), str(rated), id_movie)

				if 'actors' in IMDB_data:
					actors = IMDB_data['actors']
					addActors(cur_1, actors, id_movie)

				if 'genres' in IMDB_data:
					genres = IMDB_data['genres']
					addGenres(cur_1, genres, id_movie)

				if 'language' in IMDB_data:
					languages = IMDB_data['language']
					addLanguages(cur_1, languages, id_movie)

				keywords = theMovieDB.GetKeywords(theMovieDB_id)
				addKeywords(cur_1, keywords, id_movie)
			else:
				print "Usuwam film bo brakuje danych"
				cur_1.execute("delete from Pozycja where id_pozycja=" + id_movie + ";")	
				cur_1.execute("commit")
				removed_movies = removed_movies + 1

		else:
			print "Usuwam film bo go nie ma"
			cur_1.execute("delete from Pozycja where id_pozycja=" + id_movie + ";")	
			cur_1.execute("commit")
			removed_movies = removed_movies + 1


	czas_zakonczenia = datetime.datetime.now()

	print "Czas trwania procesu: " + str(czas_zakonczenia - czas_rozpoczecia)[2:9]
	print "Usunięto " + str(removed_movies) + " filmy"

def addKeywords(cur, keywords, id_movie):
	for keyword in keywords:
		keyword = re.escape(keyword)

		cur.execute("insert into Keyword(nazwa_keyword) select * from (select \"" + keyword + "\") as tmp where not exists(select nazwa_keyword from Keyword where nazwa_keyword = \"" + keyword + "\") limit 0,1;")
		cur.execute("commit")

		cur.execute("insert into FK_Keyword_Pozycja(id_keyword, id_pozycja) select * from (select (select id_keyword from Keyword where nazwa_keyword = '" + keyword + "'), " + id_movie + ") as tmp where not exists(select id_keyword, id_pozycja from FK_Keyword_Pozycja where id_keyword = (select id_keyword from Keyword where nazwa_keyword = '" + keyword + "') and id_pozycja = " + id_movie + ") limit 0,1;")
		cur.execute("commit")

def addLanguages(cur, languages, id_movie):
	numOfLanguages = len(languages)
	num = 0
	if(numOfLanguages > 5):
		numOfLanguages= 5
	for language in languages:
		num = num + 1
		if num > 5:
			break

		language = re.escape(language)
		
		cur.execute("insert into Jezyk(nazwa_jezyk) select * from (select \"" + language + "\") as tmp where not exists(select nazwa_jezyk from Jezyk where nazwa_jezyk = \"" + language + "\") limit 0,1;")
		cur.execute("commit")

		dom = str(DoM.calculaterDegreeOfMembership(num, numOfLanguages))

		cur.execute("insert into FK_Jezyk_Pozycja(id_jezyk, id_pozycja, DoM) select * from (select (select id_jezyk from Jezyk where nazwa_jezyk = '" + language + "'), " + id_movie + ", " + dom + ") as tmp where not exists(select id_jezyk, id_pozycja, DoM from FK_Jezyk_Pozycja where id_jezyk = (select id_jezyk from Jezyk where nazwa_jezyk = '" + language + "') and id_pozycja = " + id_movie + " and DoM = " + dom + ") limit 0,1;")
		cur.execute("commit")

def addGenres(cur, genres, id_movie):
	numOfGenres = len(genres)
	num = 0
	if(numOfGenres > 5):
		numOfGenres = 5
	for genre in genres:
		num = num + 1
		if num > 5:
			break

		genre = re.escape(genre)
		
		cur.execute("insert into Gatunek(nazwa_gatunek) select * from (select \"" + genre + "\") as tmp where not exists(select nazwa_gatunek from Gatunek where nazwa_gatunek = \"" + genre + "\") limit 0,1;")
		cur.execute("commit")

		dom = str(DoM.calculaterDegreeOfMembership(num, numOfGenres))

		cur.execute("insert into FK_Gatunek_Pozycja(id_gatunek, id_pozycja, DoM) select * from (select (select id_gatunek from Gatunek where nazwa_gatunek = '" + genre + "'), " + id_movie + ", " + dom + ") as tmp where not exists(select id_gatunek, id_pozycja, DoM from FK_Gatunek_Pozycja where id_gatunek = (select id_gatunek from Gatunek where nazwa_gatunek = '" + genre + "') and id_pozycja = " + id_movie + " and DoM = " + dom + ") limit 0,1;")
		cur.execute("commit")


def addActors(cur, actors, id_movie):
	num = 0
	numOfActors = len(actors)
	if(numOfActors > 10):
		numOfActors = 10
	for actor in actors:
		num = num + 1
		if num > 10:
			break

		actor = re.escape(actor)
		
		cur.execute("insert into Aktor(nazwa_aktor) select * from (select \"" + actor + "\") as tmp where not exists(select nazwa_aktor from Aktor where nazwa_aktor = \"" + actor + "\") limit 0,1;")
		cur.execute("commit")

		dom = str(DoM.calculaterDegreeOfMembership(num, numOfActors))

		cur.execute("insert into FK_Aktor_Pozycja(id_aktor, id_pozycja, DoM) select * from (select (select id_aktor from Aktor where nazwa_aktor = '" + actor + "'), " + id_movie + ", " + dom + ") as tmp where not exists(select id_aktor, id_pozycja, DoM from FK_Aktor_Pozycja where id_aktor = (select id_aktor from Aktor where nazwa_aktor = '" + actor + "') and id_pozycja = " + id_movie + " and DoM = " + dom + ") limit 0,1;")
		cur.execute("commit")

def updateMovie(cur, rating, runtime, ratingCount, rated, id_movie):
	cur.execute("update Pozycja set ocena = " + rating + ", czas_trwania = " + runtime + ", liczba_ocen = " + ratingCount + ", typ = '" + rated + "' where id_pozycja = " + id_movie + ";")
	cur.execute("commit")


def addCountries(cur, countries, id_movie):
	numOfCountries = len(countries)
	num = 0
	if(numOfCountries > 5):
		numOfCountries = 5
	for country in countries:
		num = num + 1
		if num > 5:
			break

		country = re.escape(country)
		
		cur.execute("insert into Panstwo(nazwa_panstwo) select * from (select \"" + country + "\") as tmp where not exists(select nazwa_panstwo from Panstwo where nazwa_panstwo = \"" + country + "\") limit 0,1;")
		cur.execute("commit")

		dom = str(DoM.calculaterDegreeOfMembership(num, numOfCountries))

		cur.execute("insert into FK_Panstwo_Pozycja(id_panstwo, id_pozycja, DoM) select * from (select (select id_panstwo from Panstwo where nazwa_panstwo = '" + country + "'), " + id_movie + ", " + dom + ") as tmp where not exists(select id_panstwo, id_pozycja, DoM from FK_Panstwo_Pozycja where id_panstwo = (select id_panstwo from Panstwo where nazwa_panstwo = '" + country + "') and id_pozycja = " + id_movie + " and DoM = " + dom + ") limit 0,1;")
		cur.execute("commit")

def addDirector(cur, directorName, id_movie):
	cur.execute("insert into Rezyser(nazwa_rezyser) select * from (select \"" + directorName + "\") as tmp where not exists(select nazwa_rezyser from Rezyser where nazwa_rezyser = \"" + directorName + "\") limit 0,1;")
	cur.execute("commit")

	cur.execute("update Pozycja set id_rezyser = (select id_rezyser from Rezyser where nazwa_rezyser = '" + directorName + "') where id_pozycja = " + str(id_movie) + ";");
	cur.execute("commit")

main()