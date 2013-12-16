<?php

require_once "bootstrap.php";

$newLocationName = $argv[1];

$location = new Location();
$location->setName( $newLocationName );

$em->persist( $location );
$em->flush();

echo 'Created Location with ID ' . $location->getId() . "\n";
