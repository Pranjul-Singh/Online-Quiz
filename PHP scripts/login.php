<?php
require_once 'functions.php';
$id = $_POST['id'];
$pass = $_POST['pass'];
$logn = new dbms;
$rslt = $logn->mysqlConnect('okquiz', "select * from organisers where oid = '".$id."' and pass = '".$pass."';");
if(mysql_num_rows($rslt)==1)
{
    echo '0';
}
else
{
    echo '1';
}