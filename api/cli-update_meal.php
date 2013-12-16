<?php
// cli-update_meal.php <id> <name> <description> <image> <price>
require_once 'bootstrap.php';

$id = $argv[1];

$name        = $argv[2];
$description = $argv[3];
$image       = $argv[4];
$price       = $argv[5];

$meal = $em->find( 'Meal', $id );

if ( $meal === null ) {
    echo "There is not meal with id: $id.\n";
    exit(1);
}

$meal->setName( $name );
$meal->setDescription( $description );
$meal->setImage( $image );
$meal->setPrice( $price );

$em->flush();
