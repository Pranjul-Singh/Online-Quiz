<?php
require_once 'functions.php';
$oid = $_GET['oid'];
$logn = new dbms;
$cd = $logn->mysqlConnect('okquiz', "select tid, tname, tdate, ttime, type, ques from tests where oid = ".$oid.";");
$count = mysql_num_rows($cd);
$arry = array();
for($i=0;$i<$count;$i++){
    $ar = array("tid"=>mysql_result($cd, $i, 0),"tname"=>mysql_result($cd, $i, 1),"date"=>mysql_result($cd, $i, 2),"time"=>mysql_result($cd, $i, 3),"type"=>mysql_result($cd, $i, 4),"ques"=>mysql_result($cd, $i, 5));
    $arry[$i] = $ar;
}
print json_encode($arry);