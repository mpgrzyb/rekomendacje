<?php
$zmienna=$_POST["q"];
	
$con = mysql_connect('95.211.178.2', 'glebels_root', 'vEn1cEqUEEn');
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("glebels_filman", $con);
mysql_query("SET NAMES 'utf8'");
$sql="Select id_pozycja, tytul_pl, plakat_mini From Pozycja group by id_pozycja, tytul_pl order by ocena desc limit 0,21;";

$result = mysql_query($sql);

$row = mysql_fetch_array($result);

while($row = mysql_fetch_array($result)){
	echo $row['id_pozycja'] . '+' . $row['tytul_pl'] . '+' .$row['plakat_mini'] . ';';
}

mysql_close($con);
?>