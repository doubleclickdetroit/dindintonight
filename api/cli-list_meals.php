<?php

require 'bootstrap.php';

$mealRepo = $em->getRepository('Meal');
$meals = $mealRepo->findAll();

foreach( $meals as $meal ) {
    echo sprintf( "-%s\n", $meal->getId() );
    echo sprintf( "--%s\n", $meal->getName() );
    echo sprintf( "--%s\n", $meal->getDescription() );
    echo sprintf( "--%s\n", $meal->getImage() );
    echo sprintf( "--%s\n", $meal->getPrice() );
}
