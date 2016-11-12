<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$qno = $_POST['qno'];
$ques = $_POST['ques'];
$op1 = $_POST['op1'];
$op2 = $_POST['op2'];
$op3 = $_POST['op3'];
$op4 = $_POST['op4'];
$ans = $_POST['ans'];
$mrks = $_POST['mrks'];
$update = new dbms;
$update->mysqlConnect('okquiz', "insert into ques values('".$tid."',".$qno.",'".$ques."','".$op1."','".$op2."','".$op3."','".$op4."',".$ans.",".$mrks.");");