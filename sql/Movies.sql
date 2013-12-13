-- Suma iloczynów stopni przynależności gatunków dwóch filmów
select sum(tmp1.DoMMultiplication) as Numerator from (select g1.nazwa_gatunek as gat1, g2.nazwa_gatunek as gat2, g1.DoM as DoM1, g2.DoM as DoM2,
	CASE 
		WHEN g1.nazwa_gatunek = g2.nazwa_gatunek THEN round(g1.DoM * g2.DoM, 5)
		WHEN g1.nazwa_gatunek != g2.nazwa_gatunek THEN 0 
	END
	as 'DoMMultiplication'
	from (select nazwa_gatunek, DoM from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Chłopcy z ferajny") as g1 
	join (select nazwa_gatunek, DoM from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Ojciec Chrzestny") as g2) as tmp1;

-- Iloczyn pierwiastków sumy kwadratów funkcji przynależności
select m1.value*m2.value as Denominator
from (select sqrt(sum(Pow(DoM, 2))) as value from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Chłopcy z ferajny") as m1
join (select sqrt(sum(Pow(DoM, 2))) as value from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Ojciec Chrzestny") as m2;

-- Funkcja licząca podobieństwo między dwoma filmami
select round(Num.Numerator/Den.Denominator, 7) as Similarity 
	from (select sum(tmp1.DoMMultiplication) as Numerator from (select g1.nazwa_gatunek as gat1, g2.nazwa_gatunek as gat2, g1.DoM as DoM1, g2.DoM as DoM2, CASE WHEN g1.nazwa_gatunek = g2.nazwa_gatunek THEN round(g1.DoM * g2.DoM, 5) WHEN g1.nazwa_gatunek != g2.nazwa_gatunek THEN 0 END as 'DoMMultiplication' from (select nazwa_gatunek, DoM from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Chłopcy z ferajny") as g1 join (select nazwa_gatunek, DoM from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Ojciec Chrzestny") as g2) as tmp1) as Num
	join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Chłopcy z ferajny") as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Gatunek as g inner join FK_Gatunek_Pozycja as fk on fk.id_gatunek = g.id_gatunek inner join Pozycja as p on p.id_pozycja = fk.id_pozycja where p.tytul_pl = "Ojciec Chrzestny") as m2) as Den;