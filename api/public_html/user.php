<?php
$app->get( '/user/:id', function ( $id ) {
    require_once '../bootstrap.php';

    $user = $entityManager->find( 'User', $id );

    if ($user === null) {
        // 404
        $app->notFound();
        return;
    }

    $return = new stdclass();
    $return->id = $user->getId();
    $return->username = $user->getName();

    echo json_encode( $return );
});
