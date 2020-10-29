<?php

function generateRandomString($length = 40) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}

require_once 'connectors/tokendb.php';

$tokennow = generateRandomString();

$query = $conn->prepare("INSERT INTO `indextokens`(`token`) VALUES (?);");
$query->bind_param('s', $tokennow);
$query->execute();

$conn->close();

die("There you go -> " . $tokennow);

?>