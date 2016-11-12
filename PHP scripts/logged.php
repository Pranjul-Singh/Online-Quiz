<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$uid = $_POST['uid'];
$update = new dbms;
$update->mysqlConnect('okquiz', "alter table ".$tid." add ".$uid." int;");
echo $tid;