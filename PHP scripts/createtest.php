<?php
require_once 'functions.php';
$tname = $_POST['tname'];
$tid = $_POST['tid'];
$oid = $_POST['oid'];
$type = $_POST['type'];
$tdate = $_POST['tdate'];
$ttime = $_POST['ttime'];
$dur = $_POST['dur'];
$ques = $_POST['ques'];
$update = new dbms;
$update->mysqlConnect('okquiz', "insert into tests values('".$tid."','".$tname."','".$oid."',".$type.",'".$tdate."','".$ttime."','".$dur."',".$ques.");");