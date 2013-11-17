<?php
// update_meal.php <id> <new-name>
require_once 'bootstrap.php';

$id = $argv[1];
$id = 1;
$description = 'Fresh salmon marinated in basil, garlic, sea salt, and olive oil, grilled and glazed with a sweet flowery honey. Served with a fluffly long grain rice';
$title = 'Glazed Salmon';

$meal = $entityManager->find('Meal', $id);

if ($meal === null) {
    echo "Meal $id does not exist.\n";
    exit(1);
}

$meal->setName( $title );
$meal->setDescription( $description );
$meal->setVegetarian(0);

$entityManager->flush();
