-- Pierwsza wersja funkcji
DROP FUNCTION `SumDoM`;
CREATE DEFINER=`glebels_root`@`localhost` FUNCTION `SumDoM`(`uzytkownikId` INT, `filmId` INT) RETURNS DECIMAL(10,7) NOT DETERMINISTIC NO SQL SQL SECURITY DEFINER return (select round(sum(Similarity*Ocena),7) from
    (select f.id_film as idFilm1, ff.id_film2 as idFilm2, ff.id_film as idFilm3, DoMLiked(uf.ocena) as 'Ocena', ff.Similarity
    from Filmy f
            inner join FK_Uzytkownicy_Filmy uf on uf.id_film = f.id_film
            inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik
            inner join FK_Filmy_Filmy ff on ff.id_film = f.id_film or ff.id_film2 = f.id_film
    where u.id_uzytkownik = uzytkownikId and ((ff.id_film = filmId and ff.id_film2 = f.id_film) or (ff.id_film2 = filmId and ff.id_film = f.id_film))
    group by f.id_film, ff.id_film2, ff.id_film, ff.Similarity 
    having Ocena > 0.5) as tmp)






-- Zmienione zapytanie na potrzeby nowej tabeli z pełnym iloczynek kartezjańskim
select f.id_film as idFilm1, ff.id_film2 as idFilm2, DoMLiked(uf.ocena) as 'Ocena', ff.Similarity
    from Filmy f
            inner join FK_Uzytkownicy_Filmy uf on uf.id_film = f.id_film
            inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik
            inner join FK_Filmy_Filmy ff on ff.id_film = f.id_film
    where u.id_uzytkownik = 1 and ff.id_film2 = 1161 and ff.id_film2 != f.id_film
    group by f.id_film, ff.id_film2, ff.Similarity 
    having Ocena > 0.5

-- Nowa funkcja sumująca iloczyny podobieństw i ocen
DROP FUNCTION `SumDoM2`;
CREATE DEFINER=`glebels_root`@`localhost` FUNCTION `SumDoM2`(`uzytkownikId` INT, `filmId` INT) RETURNS DECIMAL(10,7) DETERMINISTIC NO SQL SQL SECURITY DEFINER return (select round(sum(Similarity*Ocena),7) from
    (select f.id_film as idFilm1, ff.id_film2 as idFilm2, DoMLiked(uf.ocena) as 'Ocena', ff.Similarity
    from Filmy f
            inner join FK_Uzytkownicy_Filmy uf on uf.id_film = f.id_film
            inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik
            inner join FK_Filmy_Filmy ff on ff.id_film = f.id_film
    where u.id_uzytkownik = 1 and ff.id_film2 = 1161 and ff.id_film2 != f.id_film
    group by f.id_film, ff.id_film2, ff.Similarity 
    having Ocena > 0.5) as tmp)


-- Zapytanie do funkcji przy tabeli FK_Filmy_Filmy z pełnym iloczynem kartezjańskim
select id_film, tytul_pl, sumDoM2(1,id_film) From Filmy group by id_film, tytul_pl order by sumDoM2(1,id_film) desc limit 0,20;


select tytul_pl
from Filmy f
	inner join 