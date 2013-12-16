<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class LocationsId
{

    private $locationRepository;

    public function __construct( $locationRepository )
    {
        $this->locationRepository = $locationRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $id = $params['id'];

        $location = $this->locationRepository->find( $id );

        if ( $location === null ) {
            call_user_func( $notFound );
            /*
            $response->status(404);
            $response->body( json_encode( array( 'msg' => 'Location not found' ) ) );
             */
            return;
        }

        $response->body( json_encode( $location ) );
    }
}
