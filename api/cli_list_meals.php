<?php
require_once 'bootstrap.php';

$mealRepository = $entityManager->getRepository('Meal');
$meals = $mealRepository->findAll();

foreach ($meals as $meal) {
    echo sprintf("-%s\n", $meal->getName());
}
