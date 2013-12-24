<?php
$zmienna=$_POST["q"];
$zmienna1=$_POST["w"];
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("glebels_movies", $con);
mysql_query("SET NAMES 'utf8'");
$sql="Select count(id_uzytkownik) as count From Uzytkownicy where login = '" . stripslashes($zmienna) . "';";

$result = mysql_query($sql);

$row = mysql_fetch_array($result);
$num_of_users = $row['count'];

if($num_of_users == 0){
	$sql = "insert into Uzytkownicy(login, haslo) values('" . stripslashes($zmienna) . "', '" . stripslashes($zmienna1) . "');";
	mysql_query($sql);

	$sql = "select id_uzytkownik from Uzytkownicy where login = '" . stripslashes($zmienna) . "';";
	$result = mysql_query($sql);
	$row = mysql_fetch_array($result);
	echo $row['id_uzytkownik'];
}else{
	$sql = "select id_uzytkownik from Uzytkownicy where login = '" . stripslashes($zmienna) . "' and haslo = '" . stripslashes($zmienna1) . "';";
	$result = mysql_query($sql);
	$row = mysql_fetch_array($result);
	if($row['id_uzytkownik']!=''){
		echo $row['id_uzytkownik'];		
	}else{
		echo "false";		
	}
}
mysql_close($con);
?>