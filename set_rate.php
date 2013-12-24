<?php
$userId=$_POST["_userId"];
$movieId=$_POST["_movieId"];
$rate=$_POST["_rate"];

$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
{
	die('Could not connect: ' . mysql_error());
}

$filmy = json_decode($zmienna);

mysql_select_db("glebels_movies", $con);
mysql_query("SET NAMES 'utf8'");

$sql="insert into FK_Uzytkownicy_Filmy(id_uzytkownik, id_film, ocena) values( " . $userId . ", " . $movieId . ", " . $rate . ");";
mysql_query($sql);

mysql_close($con);
?>