# -*- coding: UTF-8 -*-
from math import sqrt, log

# Wynik 0,8
gatunki = ['Dramat', 'Gangsterski', 'Biograficzny', 'Thriller']
movie1 = { 'tytuł' : 'Ojciec chrzestny', 'ocena' : 9.1, 'gatunki' : { 'Dramat' : 0.33333, 'Gangsterski': 0.66667 }}
movie2 = { 'tytuł' : 'Chłopaki z ferajny', 'ocena' : 8.7, 'gatunki' : { 'Dramat' : 0.2, 'Gangsterski': 0.3, 'Thriller': 0.1, 'Biograficzny': 0.4 }}

# Wynik 0,247313
# gatunki = ['Crime', 'Horror', 'Mystery', 'Thriller', 'Drama']
# movie1 = { 'tytuł' : 'Copycat', 'ocena' : 7.2, 'gatunki' : { 'Crime' : 1.0 , 'Mystery' : 0.44 , 'Thriller' : 0.35, 'Drama' : 0.29 }}
# movie2 = { 'tytuł' : 'Grudge', 'ocena' : 6.9, 'gatunki' : { 'Horror' : 1.0 , 'Mystery' : 0.41 , 'Thriller' : 0.47 }}
        
def Similarity(movie1, movie2):
	sumDoM1 = 0
	sumDoM2 = 0
	sumDoM = 0
	for gatunek in gatunki:
		DoM1 = 0
		DoM2 = 0
		if gatunek in movie1['gatunki']:
			DoM1 = movie1['gatunki'][gatunek]
		if gatunek in movie2['gatunki']:
			DoM2 = movie2['gatunki'][gatunek]

		sumDoM = sumDoM + (DoM1 * DoM2)
		sumDoM1 = sumDoM1 + pow(DoM1, 2)
		sumDoM2 = sumDoM2 + pow(DoM2, 2)
	return (sumDoM)/(sqrt(sumDoM1)*sqrt(sumDoM2))

def Prediction(movie):
	return 1.0

print Similarity(movie1, movie2)