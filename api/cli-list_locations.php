<?php

require 'bootstrap.php';

$locationRepo = $em->getRepository('Location');
$locations = $locationRepo->findAll();

foreach( $locations as $location ) {
    echo sprintf( "-%s\n", $location->getId() );
    echo sprintf( "--%s\n", $location->getName() );
    echo sprintf( "--%s\n", $location->getAddress() );
    echo sprintf( "--%s\n", $location->getCity() );
    echo sprintf( "--%s\n", $location->getState() );
    echo sprintf( "--%s\n", $location->getZip() );
}
