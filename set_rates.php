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

for ($i = 0; $i < 2; $i++){
	$idFilmu = $filmy[$i][0];
	$tytul = $filmy[$i][1];
	$ocena = $filmy[$i][2];
	$login = $filmy[$i][3];
	$sql="insert into FK_Uzytkownicy_Filmy(id_uzytkownik, id_film, ocena) values((select id_uzytkownik from Uzytkownicy where login = '" . $login . "'), " . $idFilmu . ", " . $ocena . ")";
	mysql_query($sql);
}
mysql_close($con);
?>