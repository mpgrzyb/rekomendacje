DROP FUNCTION `Similarity`;
CREATE DEFINER=`glebels_root`@`localhost` FUNCTION `Similarity`(`id1` INT, `id2` INT) RETURNS DECIMAL(12,7) NOT DETERMINISTIC NO SQL SQL SECURITY DEFINER return (select round(((simGatunki.tmpSimilarity*6/10)+(simAktorzy.tmpSimilarity*2/10)+(simJezyki.tmpSimilarity*1/10)+(simPanstwa.tmpSimilarity*1/10)),7) as 'Similarity'
from 
	(select round(Num.Numerator/Den.Denominator, 7) as tmpSimilarity from (select sum(tmp1.DoMMultiplication) as Numerator from (select g1.nazwa_gatunek as gat1, g2.nazwa_gatunek as gat2, g1.DoM as DoM1, g2.DoM as DoM2, CASE WHEN g1.nazwa_gatunek = g2.nazwa_gatunek THEN round(g1.DoM * g2.DoM, 5) WHEN g1.nazwa_gatunek != g2.nazwa_gatunek THEN 0 END as 'DoMMultiplication' from (select nazwa_gatunek, DoM from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as g1 join (select nazwa_gatunek, DoM from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as g2) as tmp1) as Num join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Gatunki as g inner join FK_Gatunki_Filmy as fk on fk.id_gatunek = g.id_gatunek inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as m2) as Den)
		as simGatunki
	join (select round(Num.Numerator/Den.Denominator, 7) as tmpSimilarity from (select sum(tmp1.DoMMultiplication) as Numerator from (select a1.nazwa_aktor as akt1, a2.nazwa_aktor as akt2, a1.DoM as DoM1, a2.DoM as DoM2, CASE WHEN a1.nazwa_aktor = a2.nazwa_aktor THEN round(a1.DoM * a2.DoM, 5) WHEN a1.nazwa_aktor != a2.nazwa_aktor THEN 0 END as 'DoMMultiplication' from (select nazwa_aktor, DoM from Aktorzy as a inner join FK_Aktorzy_Filmy as fk on fk.id_aktor = a.id_aktor inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as a1 join (select nazwa_aktor, DoM from Aktorzy as a inner join FK_Aktorzy_Filmy as fk on fk.id_aktor = a.id_aktor inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as a2) as tmp1) as Num join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Aktorzy as a inner join FK_Aktorzy_Filmy as fk on fk.id_aktor = a.id_aktor inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Aktorzy as a inner join FK_Aktorzy_Filmy as fk on fk.id_aktor = a.id_aktor inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as m2) as Den)
		as simAktorzy
	join (select round(Num.Numerator/Den.Denominator, 7) as tmpSimilarity from (select sum(tmp1.DoMMultiplication) as Numerator from (select a1.nazwa_jezyk as jez1, a2.nazwa_jezyk as jez2, a1.DoM as DoM1, a2.DoM as DoM2, CASE WHEN a1.nazwa_jezyk = a2.nazwa_jezyk THEN round(a1.DoM * a2.DoM, 5) WHEN a1.nazwa_jezyk != a2.nazwa_jezyk THEN 0 END as 'DoMMultiplication' from (select nazwa_jezyk, DoM from Jezyki as a inner join FK_Jezyki_Filmy as fk on fk.id_jezyk = a.id_jezyk inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as a1 join (select nazwa_jezyk, DoM from Jezyki as a inner join FK_Jezyki_Filmy as fk on fk.id_jezyk = a.id_jezyk inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as a2) as tmp1) as Num join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Jezyki as a inner join FK_Jezyki_Filmy as fk on fk.id_jezyk = a.id_jezyk inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Jezyki as a inner join FK_Jezyki_Filmy as fk on fk.id_jezyk = a.id_jezyk inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as m2) as Den)
		as simJezyki
	join (select round(Num.Numerator/Den.Denominator, 7) as tmpSimilarity from (select sum(tmp1.DoMMultiplication) as Numerator from (select a1.nazwa_panstwo as jez1, a2.nazwa_panstwo as jez2, a1.DoM as DoM1, a2.DoM as DoM2, CASE WHEN a1.nazwa_panstwo = a2.nazwa_panstwo THEN round(a1.DoM * a2.DoM, 5) WHEN a1.nazwa_panstwo != a2.nazwa_panstwo THEN 0 END as 'DoMMultiplication' from (select nazwa_panstwo, DoM from Panstwa as a inner join FK_Panstwa_Filmy as fk on fk.id_panstwo = a.id_panstwo inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as a1 join (select nazwa_panstwo, DoM from Panstwa as a inner join FK_Panstwa_Filmy as fk on fk.id_panstwo = a.id_panstwo inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as a2) as tmp1) as Num join (select m1.value*m2.value as Denominator from (select sqrt(sum(Pow(DoM, 2))) as value from Panstwa as a inner join FK_Panstwa_Filmy as fk on fk.id_panstwo = a.id_panstwo inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id2) as m1 join (select sqrt(sum(Pow(DoM, 2))) as value from Panstwa as a inner join FK_Panstwa_Filmy as fk on fk.id_panstwo = a.id_panstwo inner join Filmy as f on f.id_film = fk.id_film where f.id_film = id1) as m2) as Den)
		as simPanstwa)