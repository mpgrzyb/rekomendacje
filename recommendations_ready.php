<?php
$userId=$_POST["_userId"];
	
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("glebels_movies", $con);
mysql_query("SET NAMES 'utf8'");
$sql="Select count(id_film) from FK_Uzytkownicy_Filmy where id_uzytkownik =" . stripslashes($userId) . " and ocena > 0;";
$result = mysql_query($sql);

while($row = mysql_fetch_array($result)){
	echo $row['count(id_film)'];
}

mysql_close($con);
?>