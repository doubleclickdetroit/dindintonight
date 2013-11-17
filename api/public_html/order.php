<?php
$app->post( '/order', function() use ( $app ) {
    require_once '../bootstrap.php';

    $user = $app->request->post('user');

    if ( $user === null ) {
        $app->response->setStatus('401');
        $app->response->write('BAD REQUEST');
        return;
    }

    $user = json_decode( $user );
    if ( !property_exists( $user, 'user_id' ) ) {
        // create user, assign $user_id
    }
    $user_id = $user->user_id;

    $location = $app->request->post('location');

    if ( $location === null ) {
        $app->response->setStatus('402');
        $app->response->write('BAD REQUEST');
        return;
    }

    $location = json_decode( $location );
    if ( !property_exists( $location, 'location_id' ) ) {
        // create location, assign $location_id
    }
    $location_id = $location->location_id;

    $meals = $app->request->post('meals');

    if ( $meals === null ) {
        $app->response->setStatus('403');
        $app->response->write('BAD REQUEST');
        return;
    }

    $meals = json_decode( $meals );

    if ( count( $meals->meals ) < 1 || count( $meals->meals ) > 2 ) {
        $app->response->setStatus('405');
        $app->response->write('BAD REQUEST');
        return;
    }

    $payment = $app->request->post('payment');

    if ( $payment === null && false ) {
        $app->response->setStatus('406');
        $app->response->write('BAD REQUEST');
        return;
    }

    $drop = new Drop();
    $drop->setUserId( $user_id );
    $drop->setLocationId( $location_id );

    $entityManager->persist( $drop );
    $entityManager->flush();

    foreach( $meals->meals as $meal ) {
        $dropMeal = new DropMeal();
        $dropMeal->setDropId( $drop->getId() );
        $dropMeal->setMealId( $meal->meal_id );
        $dropMeal->setQuantity( $meal->quantity );

        $entityManager->persist( $dropMeal );
        $entityManager->flush();
    }

    $return = new stdclass();
    $return->order_id = $drop->getId();

    echo json_encode( $return );
});
