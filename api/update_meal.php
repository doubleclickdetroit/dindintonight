<?php
// update_meal.php <id> <new-name>
require_once 'bootstrap.php';

$id = $argv[1];
$newName = $argv[2];

$meal = $entityManager->find('Meal', $id);

if ($meal === null) {
    echo "Meal $id does not exist.\n";
    exit(1);
}

$meal->setName($newName);

$entityManager->flush();
