<?php
$app->get( '/meal', function () {
    require_once '../bootstrap.php';

    $meals = $entityManager->getRepository('Meal')->findBy(array('status' => 'ACTIVE'));

    $return = array();
    foreach( $meals as $meal ) {
        $entry = new stdclass();
        $entry->id          = $meal->getId();
        $entry->title       = $meal->getName();
        $entry->photo       = $meal->getImage();
        $entry->description = $meal->getDescription();
        $entry->coins       = '1';
        $entry->vegetarian  = $meal->getVegetarian();
        $entry->quantity    = 0;
        $return[] = $entry;
    }

    echo json_encode( $return );
});
