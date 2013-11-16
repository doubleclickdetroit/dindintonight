<?php
$app->post( '/order', function() use ( $app ) {
    require_once '../bootstrap.php';

    $user        = $app->request->post('user');
    $user_id     = $app->request->post('user_id');

    // if !user and !user_id

    $location    = $app->request->post('location');
    $location_id = $app->request->post('location_id');

    // if !location and !location_id

    $meals       = $app->request->post('meals');

    // Check user

    $payment     = $app->request->post('payment');

    $return = new stdclass();

    echo json_encode( $return );
});
