<?php
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

require '../vendor/autoload.php';


$isDevMode = true;
$config = Setup::createAnnotationMetadataConfiguration( array( __DIR__ . '/src' ), $isDevMode);

// the connection configuration
$dbParams = array(
    'driver'   => 'pdo_mysql',
    'user'     => 'dindintonight',
    'password' => 'dindintonight',
    'dbname'   => 'dindintonight',
);

$em = EntityManager::create( $dbParams, $config );


$app      = new \Slim\Slim( array( 'debug' => true ) );
$response = $app->response;
$response['Content-Type'] = 'application/json';



// Locations //
$app->get('/locations', function() use ( $response, $em ) {
    $locationRepo = $em->getRepository('Location');
    $locations    = $locationRepo->findAll();

    foreach( $locations as $location ) {
        $data[] = createLocationObject( $location );
    }

    $response->status(200);
    $response->body( json_encode( $data ) );
});

$app->get('/locations/:id', function( $id ) use ( $response, $em ) {
    $location = $em->find( 'Location', $id );

    if ( $location === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'Location not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createLocationObject( $location ) ) );
});

$app->get('/locations/:id/meals', function( $id ) use ( $response, $em ) {
    $location = $em->find( 'Location', $id );

    if ( $location === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'Location not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createMealObjectsFromLocation( $location ) ) );
});

$app->get('/locations/:id/drops', function( $id ) use ( $response, $em ) {
    $location = $em->find( 'Location', $id );

    if ( $location === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'Location not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createDropObjectsFromLocation( $location ) ) );
});
// End Locations //

// Meals //
$app->get('/meals', function() use ( $response, $em ) {
    $mealRepo = $em->getRepository('Meal');
    $meals    = $mealRepo->findAll();

    foreach( $meals as $meal ) {
        $data[] = createMealObject( $meal );
    }

    $response->status(200);
    $response->body( json_encode( $data ) );
});

$app->get('/meals/:id', function( $id ) use ( $response, $em ) {
    $meal = $em->find( 'Meal', $id );

    if ( $meal === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'Meal not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createMealObject( $meal ) ) );
});
// End Meals //

// Addresses //
$app->get('/addresses', function() use( $response, $em ) {
    $addressRepo = $em->getRepository('Address');
    $addresses   = $addressRepo->findAll();

    foreach( $addresses as $address ) {
        $data[] = createAddressObject( $address );
    }
    $response->status(200);
    $response->body( json_encode( $data ) );
});

$app->get('/addresses/:id', function( $id ) use ( $response, $em ) {
    $address = $em->find( 'Address', $id );

    if ( $address === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'Address not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createAddressObject( $address ) ) );

});
// End Addresses //


// Users //
$app->get('/users', function() use( $response, $em ) {
    $userRepo = $em->getRepository('User');
    $users   = $userRepo->findAll();

    foreach( $users as $user ) {
        $data[] = createUserObject( $user );
    }
    $response->status(200);
    $response->body( json_encode( $data ) );
});

$app->get('/users/:id', function( $id ) use ( $response, $em ) {
    $user = $em->find( 'User', $id );

    if ( $user === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'User not found' ) ) );
        return;
    }

    $response->status(200);
    $response->body( json_encode( createUserObject( $user ) ) );

});

$app->put('/users/:id', function( $id ) use ( $response, $em ) {
    $user = $em->find( 'User', $id );

    if ( $user === null ) {
        $response->status(404);
        $response->body( json_encode( array( 'msg' => 'User not found' ) ) );
        return;
    }

//@todo: finish

});
// End Users //


function createLocationObject( $location )
{
    $info = array();

    $info['id']      = $location->getId();
    $info['name']    = $location->getName();
    $info['address'] = $location->getAddress();
    $info['city']    = $location->getCity();
    $info['state']   = $location->getState();
    $info['zip']     = $location->getZip();

    return $info;
}

function createMealObject( $meal )
{
    $info = array();

    $info['id']          = $meal->getId();
    $info['name']        = $meal->getName();
    $info['description'] = $meal->getDescription();
    $info['image']       = $meal->getImage();
    $info['price']       = $meal->getPrice();

    return $info;
}

function createAddressObject( $address )
{
    $info = array();

    $info['id']          = $address->getId();
    $info['address']     = $address->getAddress();
    $info['location_id'] = $address->getLocation()->getId();

    return $info;
}

function createCardObject( $card )
{
    $info = array();

    $info['id']    = $card->getId();
    $info['last4'] = $card->getLast4();

    return $info;
}

function createUserObject( $user )
{
    $info = array();

    $info['id']             = $user->getId();
    $info['firstName']      = $user->getFirstName();
    $info['lastName']       = $user->getLastName();
    $info['email']          = $user->getEmail();
    $info['addresses']      = array();
    $info['cards']          = array();
    $info['facebook_token'] = '';
    $info['facebook_id']    = '';

    foreach( $user->getAddresses() as $address ) {
        $info['addresses'][] = createAddressObject( $address );
    }

    foreach( $user->getCards() as $card ) {
        $info['cards'][] = createCardObject( $card );
    }

    return $info;
}

function createMealObjectsFromLocation( $location )
{
    $info = array();

    foreach( $location->getMeals() as $meal ) {
        $info[] = createMealObject( $meal );
    }

    return $info;
}

function createDropObjectsFromLocation( $location )
{
    return 'not yet finished';
    $info = array();

    // look up all drops from today with given location
    $drops = $em->find( 'Location', $id );

    foreach( $location->getId as $id ) {

    }

    return $info;
}


$app->run();
