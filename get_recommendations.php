<?php
$userId=$_POST["_userId"];

$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
{
	die('Could not connect: ' . mysql_error());
}

$filmy = json_decode($zmienna);

mysql_select_db("glebels_movies", $con);
mysql_query("SET NAMES 'utf8'");

$sql="select id_film, tytul_pl, Year(rok_produkcji) as rok, ((sumDoM2(" . $userId . ",id_film)*75/100)+(f.ocena/10*25/100)) as Prognoza From Filmy f where id_film not in (select f.id_film from FK_Uzytkownicy_Filmy uf inner join Filmy f on f.id_film = uf.id_film inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik where u.id_uzytkownik=" . $userId . "  and uf.ocena != -1) group by tytul_pl order by sumDoM2(" . $userId . ",id_film) desc, f.ocena desc, f.popularnosc desc limit 0,15;";

$result = mysql_query($sql);
$row = mysql_fetch_array($result);
echo '<div id="header_1">TWOJE REKOMENDACJE</div>';

while($row = mysql_fetch_array($result)){
	echo '<div id="movie">' . $row['tytul_pl'] . ' (' . $row['rok'] . ')</div>';
}

mysql_close($con);
?>