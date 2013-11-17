<?php
$zmienna=$_POST["q"];
	
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("glebels_filman", $con);
mysql_query("SET NAMES 'utf8'");
$sql="Select count(id_uzytkownik) as count From Uzytkownik where login = '" . stripslashes($zmienna) . "';";

$result = mysql_query($sql);

$row = mysql_fetch_array($result);
$num_of_users = $row['count'];

if($num_of_users == 0){
	$sql = "insert into Uzytkownik(login) values('" . stripslashes($zmienna) . "');";
	mysql_query($sql);
	echo "true";
}else{
	echo "false";
}
mysql_close($con);
?>