<?php
$app->get( '/coin', function () {
    $return = array(
        '1' => '10.00',
        '2' => '18.00',
    );

    echo json_encode( $return );
});
