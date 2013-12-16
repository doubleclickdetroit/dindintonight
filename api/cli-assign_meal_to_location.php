<?php

require_once 'bootstrap.php';

$locationId = $argv[1];
$mealId     = $argv[2];

$location = $em->find( 'Location', $locationId );
$meal     = $em->find( 'Meal', $mealId );

$location->addMeal( $meal );

$em->persist( $location );
$em->flush();

echo 'Updated Location with ID ' . $location->getId() . "\n";
