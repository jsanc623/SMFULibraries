<?php

require("SMFUShorten.php");

$apiKey = "";
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
