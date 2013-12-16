<?php
// cli-update_location.php <id> <address> <city> <state> <zip>
require_once 'bootstrap.php';

$id = $argv[1];

$address = $argv[2];
$city    = $argv[3];
$state   = $argv[4];
$zip     = $argv[5];

$location = $em->find( 'Location', $id );

if ( $location === null ) {
    echo "There is not location with id: $id.\n";
    exit(1);
}

$location->setAddress( $address );
$location->setCity( $city );
$location->setState( $state );
$location->setZip( $zip );

$em->flush();
