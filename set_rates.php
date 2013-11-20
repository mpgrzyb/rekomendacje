<?php
$zmienna=$_POST["q"];
	
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
{
	die('Could not connect: ' . mysql_error());
}

$array = json_decode($zmienna);

mysql_select_db("glebels_filman", $con);
mysql_query("SET NAMES 'utf8'");
echo($array[0][2]);
mysql_close($con);
?>