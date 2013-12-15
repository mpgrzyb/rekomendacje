# -*- coding: UTF-8 -*-
import MySQLdb
import login
import datetime

def main():
	db = MySQLdb.connect(host=login.GetHost(), user=login.GetUser(), passwd=login.GetPassword(), db=login.GetDataBase(), charset = "utf8", use_unicode = True)
	cur = db.cursor()
	cur_1 = db.cursor()
	cur.execute("select id_film from Filmy order by id_film;")
	
	czas_rozpoczecia = datetime.datetime.now()
	count = 0
	for row1 in cur:
		for row2 in cur:
			# if row2[0] > row1[0]:
			cur_1.execute("insert into FK_Filmy_Filmy values(" + str(row1[0]) + "," + str(row2[0]) + ",Similarity(" + str(row1[0]) + "," + str(row2[0]) + "));")
			cur_1.execute("commit")
			count = count + 1
			print count
				# if count == 105:
					# print row1[0], row2[0]					
	czas_zakonczenia = datetime.datetime.now()
	print "Czas trwania procesu: " + str(czas_zakonczenia - czas_rozpoczecia)[2:9]

main()