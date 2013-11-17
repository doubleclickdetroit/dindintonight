<?php
require_once 'bootstrap.php';

$meals = $entityManager->getRepository('Meal')->findBy(array('status' => 'ACTIVE'));
/*
foreach ($meals as $meal) {
    echo sprintf("-%s\n", $meal->getName());
}
