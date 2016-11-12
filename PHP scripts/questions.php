<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$logn = new dbms;
$cd = $logn->mysqlConnect('okquiz', "select qno, ques, op1, op2, op3, op4, mrks from ques where tid = '".$tid."';");
$count = mysql_num_rows($cd);
$arry = array();
for($i=0;$i<$count;$i++){
    $ar = array("qno"=>mysql_result($cd, $i, 0),"ques"=>mysql_result($cd, $i, 1),"op1"=>mysql_result($cd, $i, 2),"op2"=>mysql_result($cd, $i, 3),"op3"=>mysql_result($cd, $i, 4),"op4"=>mysql_result($cd, $i, 5),"mrks"=>mysql_result($cd, $i, 6));
    $arry[$i] = $ar;
}
print json_encode($arry);