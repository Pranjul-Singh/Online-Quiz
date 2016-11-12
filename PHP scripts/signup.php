<?php
require_once 'functions.php';
$name = $_POST['name'];
$id = $_POST['id'];
$pass = $_POST['pass'];
$email = $_POST['email'];
$phone = $_POST['phone'];
$des = $_POST['des'];
$update = new dbms;
$update->mysqlConnect('okquiz', "insert into organisers values('".$name."','".$id."','".$pass."','".$email."','".$phone."','".$des."');");
echo $name;