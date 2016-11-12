<?php
require_once 'functions.php';
$sid = $_POST['sid'];
$tid = $_POST['tid'];
$pass = $_POST['pass'];
$logn = new dbms;
$cd = $logn->mysqlConnect('okquiz', "select stname, dob from student where sid = '".$sid."' and stpass = '".$pass."';");
$arry = array();
$arry["sid"] = $sid;
$arry["tid"] = $tid;
$arry["sname"] = mysql_result($cd, 0, 0);
$arry["dob"] = mysql_result($cd, 0, 1);

$cd1 = $logn->mysqlConnect('okquiz', "select sum(mrks) from ques where tid = '".$tid."';");
$arry["maxmrks"]=mysql_result($cd1, 0, 0);

$cd2 = $logn->mysqlConnect('okquiz', "select sum(a.mrks) from ques a, ".$tid." b where b.".$sid."=a.ans;");
$arry["minmrks"]=mysql_result($cd2, 0, 0);
/*
for($i=0;$i<$count;$i++){
    $ar = array("qno"=>mysql_result($cd, $i, 0),"ques"=>mysql_result($cd, $i, 1),"op1"=>mysql_result($cd, $i, 2),"op2"=>mysql_result($cd, $i, 3),"op3"=>mysql_result($cd, $i, 4),"op4"=>mysql_result($cd, $i, 5),"mrks"=>mysql_result($cd, $i, 6));
    $arry[$i] = $ar;
}
*/
print json_encode($arry);