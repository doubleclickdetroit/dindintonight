<?php
$app->get( '/meal', function () {
    require_once '../bootstrap.php';

    $meals = $entityManager->getRepository('Meal')->findBy(array('status' => 'ACTIVE'));

    $return = array();
    foreach( $meals as $meal ) {
        $entry = new stdclass();
        $entry->id          = $meal->getId();
        $entry->photo       = 'http://fostercityvillage.org/wp-content/uploads/2012/10/meal-m.jpg';
        $entry->description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.';
        $entry->coins       = '2';
        $entry->vegetarian  = $meal->getVegetarian();
        $return[] = $entry;
    }

    echo json_encode( $return );
});
