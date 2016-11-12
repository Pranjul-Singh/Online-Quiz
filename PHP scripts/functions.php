<?php
    class dbms {
    public function mysqlConnect($dbName,$query) {
        mysql_connect('localhost', 'root', '');
        mysql_select_db($dbName);
        $result = mysql_query($query);
        return $result;
    }
    }
    /*
    $db = new dbms;
    $re = $db->mysqlConnect('abc', 'select * from login;');
    $count = mysql_num_rows($re);
    for($i=0;$i<$count;$i++)
    {
        echo 'Name : ',mysql_result($re, $i, 0)," Password : ",  mysql_result($re, $i, 1),"<br>";
    }
     */

