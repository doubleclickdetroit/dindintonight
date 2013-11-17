<?php
require_once 'bootstrap.php';

$newMealName = $argv[1];

$mail = new Meal();
$mail->setName( $newMealName );

$entityManager->persist( $mail );
$entityManager->flush();

echo "Created Meal with ID " . $mail->getId() . "\n";
