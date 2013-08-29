<?php

require("SMFUShorten.php");

$apiKey = "a449b5dd070a10be0fbffbef5cb2484888ac49e656272498833e3df3e92d86f7";
$urlToShorten = "http://google.com";

# Just the URL String
$SMFU = new SMFU($urlToShorten, $apiKey, TRUE);
$response = $SMFU->get();

echo "<pre>";
print_r($response);
/**
 *
 * http://smfu.in/JovLrL
 *
*-*/



# Give us back the whole array
$SMFU = new SMFU($urlToShorten, $apiKey);
$response = $SMFU->get();

echo "<pre>";
print_r($response);
/**
 *
 * Array
 * (
 *     [id] => 5
 *     [urlkey] => JovLrL
 *     [url] => http://google.com
 *     [time] => 1377626555
 *     [cabal] => http://smfu.in/JovLrL
 * )
 *
*-*/
