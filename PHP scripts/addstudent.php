<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$sid = $_POST['sid'];
$sname = $_POST['sname'];
$pwd = $_POST['pwd'];
$dob = $_POST['dob'];
$update = new dbms;
$update->mysqlConnect('okquiz', "insert into student values('".$tid."','".$sid."','".$sname."','".$pwd."','".$dob."');");