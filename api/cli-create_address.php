<?php

require_once 'bootstrap.php';

$addressName = $argv[1];
$locationId = $argv[2];

$location = $em->find( 'Location', $locationId );

$address = new Address();
$address->setAddress( $addressName );
$address->setLocation( $location );

$em->persist( $address );
$em->flush();

echo 'Created Address with ID ' . $address->getId() . "\n";
