<?php
$zmienna=$_POST["q"];
	
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
{
	die('Could not connect: ' . mysql_error());
}

$filmy = json_decode($zmienna);

mysql_select_db("glebels_movies", $con);
mysql_query("SET NAMES 'utf8'");

$userId = $filmy[0][3];
for ($i = 0; $i < count($filmy); $i++){
	$idFilmu = $filmy[$i][0];
	$tytul = $filmy[$i][1];
	$ocena = $filmy[$i][2];
	if($ocena!=''){
	echo 'idzie';

		$sql="insert into FK_Uzytkownicy_Filmy(id_uzytkownik, id_film, ocena) values( " . $userId . ", " . $idFilmu . ", " . $ocena . ")";
		echo $sql;
		mysql_query($sql);
	}
}

$sql="select id_film, tytul_pl, Year(rok_produkcji) as rok, f.ocena, sumDoM2(" . $userId . ",id_film) as DoM From Filmy f where id_film not in (select f.id_film from FK_Uzytkownicy_Filmy uf inner join Filmy f on f.id_film = uf.id_film inner join Uzytkownicy u on u.id_uzytkownik = uf.id_uzytkownik where u.id_uzytkownik=" . $userId . ") group by id_film, tytul_pl order by sumDoM2(" . $userId . ",id_film) desc, f.ocena desc, f.popularnosc desc limit 0,15;";
$result = mysql_query($sql);
$row = mysql_fetch_array($result);

echo "TWOJE REKOMENDACJE:";
while($row = mysql_fetch_array($result)){
	echo "   " . $row['tytul_pl'] . ' (' . $row['rok'] . ')<br>';
	// echo $row['tytul_pl'] . ' (' . $row['rok'] . ') ' .$row['DoM'] . '<br>';
}

mysql_close($con);
?>