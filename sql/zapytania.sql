-- najciekawsze dane z updateowanych Pozycji
select p.tytul_pl, p.czas_trwania, a.nazwa_aktor, fk.DoM, p.typ from Pozycja as p left join FK_Aktor_Pozycja as fk on fk.id_pozycja = p.id_pozycja left join Aktor as a on a.id_aktor = fk.id_aktor group by p.tytul_pl, a.nazwa_aktor, fk.DoM, p.czas_trwania order by p.id_pozycja asc limit 0,50;

-- rozbudowane zapytanie z GATUNKIEM i AKTORAMI
 select p.tytul_pl, p.czas_trwania, a.nazwa_aktor, fk.DoM as "DoM Aktora", p.typ, g.nazwa_gatunek, fk_g.DoM as "DoM Gatunmku" from Pozycja as p left join FK_Aktor_Pozycja as fk on fk.id_pozycja = p.id_pozycja left join Aktor as a on a.id_aktor = fk.id_aktor left join FK_Gatunek_Pozycja as fk_g on fk_g.id_pozycja = p.id_pozycja left join Gatunek as g on g.id_gatunek = fk_g.id_gatunek group by p.tytul_pl, a.nazwa_aktor, fk.DoM, fk_g.Dom, g.nazwa_gatunek, p.czas_trwania order by p.id_pozycja asc limit 0,50;

-- tworzenie nowej tabeli Filmy - Filmy (wiele do wielu)
CREATE TABLE IF NOT EXISTS `FK_Filmy_Filmy` (
  `id_film` int(11) NOT NULL,
  `id_film2` int(11) NOT NULL,
  `Similarity` decimal(10,7) DEFAULT NULL,
  PRIMARY KEY (`id_film`,`id_film2`),
  FOREIGN KEY (`id_film`) REFERENCES `Filmy`(`id_film`),
  FOREIGN KEY (`id_film2`) REFERENCES `Filmy`(`id_film`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- Przykładowe zapytanie do powyższej tabeli
select ff.Similarity
from Filmy as f
	inner join FK_Filmy_Filmy as ff on f.id_film = ff.id_film
WHERE (f.id_film = 1161 and ff.id_film2 = 1126) or (f.id_film = 1126 and ff.id_film2 = 1161);






-- Wartości w zapytaniu które generowały błąd SQL
insert into FK_Filmy_Filmy values(348,355, (select round(Num.Numerator/Den.Denominator, 5) as Similarity from (select sum(tmp1.DoMMultiplication) as Numerator from (select g1.nazwa_gatunek as gat1, g2.nazwa_gatunek as gat2, g1.DoM as DoM1, g2.DoM as DoM2, CASE WHEN g1.nazwa_gatunek = g2.nazwa_gatunek THEN round(g1.DoM * g2.DoM, 5) WHEN g1.nazwa_gatunek != g2.nazwa_gatunek THEN 0 END as 'DoMMultiplication' from (select nazwa_gatunek, DoM from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = 355) as g1 join (select nazwa_gatunek, DoM from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = 348) as g2) as tmp1) as Num join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = 355) as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = 348) as m2) as Den));