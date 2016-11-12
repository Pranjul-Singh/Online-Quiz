<?php
require_once 'functions.php';
$logn = new dbms;
$cd = $logn->mysqlConnect('okquiz', "select tid, tname, ques, type from tests;");
$count = mysql_num_rows($cd);
$arry = array();
for($i=0;$i<$count;$i++){
    $ar = array("tid"=>mysql_result($cd, $i, 0),"tname"=>mysql_result($cd, $i, 1),"ques"=>mysql_result($cd, $i, 2),"type"=>mysql_result($cd, $i, 3));
    $arry[$i] = $ar;
}
print json_encode($arry);