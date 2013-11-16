<?php
$app->get( '/user', function () {
    $return = array();

    echo json_encode( $return );
});
