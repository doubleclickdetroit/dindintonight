<?php
require_once 'bootstrap.php';

$id = $argv[1];
$drop = $entityManager->find('Drop', $id);

if ($drop === null) {
    echo "No drop found.\n";
    exit(1);
}

$dropmeals = $entityManager->getRepository('DropMeal')->findBy(array('drop_id' => $id));

foreach ($dropmeals as $dropmeal) {
    echo sprintf("-%s was ordered %d times\n", $dropmeal->getId(), $dropmeal->getQuantity());
}
