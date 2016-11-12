<?php
require_once 'functions.php';
$update = new dbms;
$update->mysqlConnect('okquiz', "create table sasdf(qno int);");
for($i=1;$i<=5;$i++)
{
    $update->mysqlConnect('okquiz', "insert into sasdf values(".$i.");");
}