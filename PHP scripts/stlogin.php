<?php
require_once 'functions.php';
$id = $_POST['id'];
$pass = $_POST['pass'];
$tid = $_POST['tid'];
$logn = new dbms;
$rslt = $logn->mysqlConnect('okquiz', "select * from student where sid = '".$id."' and stpass = '".$pass."' and tid = '".$tid."';");
if(mysql_num_rows($rslt)==1)
{
    echo '0';
}
else
{
    echo '1';
}