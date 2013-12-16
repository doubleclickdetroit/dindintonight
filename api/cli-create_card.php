<?php

require_once 'bootstrap.php';

$stripeId = $argv[1];
$last4    = $argv[2];

$card = new Card();
$card->setStripeId( $stripeId );
$card->setLast4( $last4 );

$em->persist( $card );
$em->flush();

echo 'Created Credit Card with ID ' . $card->getId() . "\n";
