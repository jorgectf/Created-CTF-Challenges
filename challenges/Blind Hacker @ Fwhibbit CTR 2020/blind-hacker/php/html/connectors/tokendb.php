<?php

if (basename($_SERVER['PHP_SELF']) === "mysql.php") { die(); }

$dbuser ='readuser';
$dbpass ='readuserpassword';
$dbname ="tokenDB";
$host = 'mysql_net';

$conn = new mysqli($host, $dbuser, $dbpass, $dbname);

if ($conn->connect_error) {
    die("Connection to the database failed, please contact an admin. This is not a drill.");
}

?>
