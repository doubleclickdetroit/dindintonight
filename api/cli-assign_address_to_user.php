<?php

require_once 'bootstrap.php';

$userId    = $argv[1];
$addressId = $argv[2];

$user    = $em->find( 'User', $userId );
$address = $em->find( 'Address', $addressId );

$user->addAddress( $address );

$em->persist( $user );
$em->flush();

echo 'Updated User with ID ' . $user->getId() . "\n";
