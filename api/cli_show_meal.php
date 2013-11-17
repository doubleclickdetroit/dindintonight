<?php
require_once 'bootstrap.php';

$id = $argv[1];
$meal = $entityManager->find('Meal', $id);

if ($meal === null) {
    echo "No meal found.\n";
    exit(1);
}

echo sprintf("-%s\n", $meal->getName());
