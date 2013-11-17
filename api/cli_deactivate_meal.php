<?php
// update_meal.php <id>
require_once 'bootstrap.php';

$id = $argv[1];

$meal = $entityManager->find('Meal', $id);

if ($meal === null) {
    echo "Meal $id does not exist.\n";
    exit(1);
}

$meal->setStatus('INACTIVE');

$entityManager->flush();
