<?php

require_once 'bootstrap.php';

$userId = $argv[1];
$cardId = $argv[2];

$user = $em->find( 'User', $userId );
$card = $em->find( 'Card', $cardId );

$user->addCard( $card );

$em->persist( $user );
$em->flush();

echo 'Updated User with ID ' . $user->getId() . "\n";
