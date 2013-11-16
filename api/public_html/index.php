<?php
require '../vendor/autoload.php';

$app = new \Slim\Slim( array( 'debug' => true ) );

include 'meal.php';
include 'coin.php';
include 'user.php';

$app->run();
