<?php
//cli-create_drop.php '2013-12-15 20:00' <location_id>

require_once 'bootstrap.php';

$dateAndTime = $argv[1];
$locationId  = $argv[2];

$location = $em->find( 'Location', $locationId );

$drop = new Drop( new DateTime( $dateAndTime )  );
$drop->setLocation( $location );

$em->persist( $drop );
$em->flush();

echo 'Created Drop with ID ' . $drop->getId() . "\n";
