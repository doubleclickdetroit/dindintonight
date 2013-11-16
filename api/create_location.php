<?php
// create_location.php <user_id>
require_once 'bootstrap.php';

$userId = $argv[1];

$user = $entityManager->find('User', $userId);

if (!$user) {
    echo "No user found for the input.\n";
    exit(1);
}

$address = '1050 Woodward Ave';
$city = 'Detroit';
$state = 'MI';
$zip = '48826';

$location = new Location();
$location->setAddress( $address );
$location->setCity( $city );
$location->setState( $state );
$location->setZip( $zip );

foreach ( $productIds AS $productId ) {
    $product = $entityManager->find("Product", $productId);
    $location->assignToProduct($product);
}

$location->setReporter($reporter);
$location->setEngineer($engineer);

$entityManager->persist($location);
$entityManager->flush();

echo "Your new Location Id: ".$location->getId()."\n";
