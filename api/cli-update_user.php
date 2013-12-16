<?php
// cli-update_user.php <id> <firstName> <lastName> <email> <stripe_token> <facebook_token> <facebook_id>
require_once 'bootstrap.php';

$id = $argv[1];

$firstName     = $argv[2];
$lastName      = $argv[3];
$email         = $argv[4];
$stripeToken   = $argv[5];
$facebookToken = $argv[6];
$facebookId    = $argv[7];

$user = $em->find( 'User', $id );

if ( $user === null ) {
    echo "There is not user with id: $id.\n";
    exit(1);
}

$user->setFirstName( $firstName );
$user->setLastName( $lastName );
$user->setEmail( $email );
$user->setStripeToken( $stripeToken );
$user->setFacebookToken( $facebookToken );
$user->setFacebookId( $facebookId );

$em->flush();
