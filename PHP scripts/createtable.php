<?php
require_once 'functions.php';
$tid = $_POST['tid'];
$ques = $_POST['ques'];
$update = new dbms;
$update->mysqlConnect('okquiz', "create table ".$tid."(qno int);");
for($i=1;$i<=$ques;$i++)
{
    $update->mysqlConnect('okquiz', "insert into ".$tid." values(".$i.");");
}
echo $tid;