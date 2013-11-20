-- średnia data produkcji

select  DATE(FROM_UNIXTIME(AVG(UNIX_TIMESTAMP(rok_produkcji)))) from Pozycja as p inner join FK_Uzytkownik_Pozycja as fk_up on fk_up.id_pozycja = p.id_pozycja  where id_uzytkownik = 3;