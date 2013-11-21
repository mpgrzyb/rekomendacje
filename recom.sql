-- średnia ważona data produkcji
select (SUM(YEAR(rok_produkcji)*fk_up.ocena)/SUM(fk_up.ocena)) from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja  where id_uzytkownik = 3;

-- średnia ważona popularność
select ROUND((SUM(p.popularnosc*fk_up.ocena)/SUM(fk_up.ocena)), 3) as 'Średnia popularność' from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja  where id_uzytkownik = 3;

-- średni czas trwania
select ROUND((SUM(p.popularnosc*fk_up.ocena)/SUM(fk_up.ocena)), 3) as 'Średnia popularność' from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja  where id_uzytkownik = 3;



-- Pierwsza funkcja
DELIMITER $$
CREATE FUNCTION AVG_ReleaseYear(userId int)
RETURNS FLOAT
BEGIN
DECLARE avgReleaseYear FLOAT default 0;
select (SUM(YEAR(rok_produkcji)*fk_up.ocena)/SUM(fk_up.ocena)) into avgReleaseYear from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja where id_uzytkownik = userId;
RETURN avgReleaseYear;
END$$;


-- Druga funkcja
DELIMITER $$
CREATE FUNCTION AVG_Popularity(userId int)
RETURNS FLOAT
BEGIN
DECLARE avgPopularity FLOAT default 0;
select ROUND((SUM(p.popularnosc*fk_up.ocena)/SUM(fk_up.ocena)), 3) into avgPopularity from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja  where id_uzytkownik = userId;
RETURN avgPopularity;
END$$;