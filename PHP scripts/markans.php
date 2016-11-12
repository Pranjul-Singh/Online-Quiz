<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$uid = $_POST['uid'];
$ans = $_POST['ans'];
$qno = $_POST['qno'];
$update = new dbms;
$update->mysqlConnect('okquiz', "update ".$tid." set ".$uid." = ".$ans." where qno = ".$qno.";");
echo $tid;