-- Zapytanie do funkcji przy tabeli FK_Filmy_Filmy z pełnym iloczynem kartezjańskim
select id_film, tytul_pl, f.ocena, sumDoM2(23,id_film) 
From Filmy f 
where id_film not in (select f.id_film from FK_Uzytkownicy_Filmy uf inner join Filmy f on f.id_film = uf.id_film inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik where u.id_uzytkownik=23) 
group by id_film, tytul_pl 
order by sumDoM2(23,id_film) desc, f.ocena desc, f.popularnosc desc
limit 0,23;	