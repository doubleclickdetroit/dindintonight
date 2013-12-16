<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class LocationsIdDrops
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
            return;
        }

        $data = array();

        /*
        foreach( $location->getDrops() as $drop ) {
            $data[] = $drop;
        }
         */

        $response->body( json_encode( $data ) );
    }
}
