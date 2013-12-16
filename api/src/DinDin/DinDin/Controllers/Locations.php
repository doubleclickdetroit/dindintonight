<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class Locations
{

    private $locationRepository;

    public function __construct( $locationRepository )
    {
        $this->locationRepository = $locationRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $data = array();

        foreach( $this->locationRepository->findAll() as $location ) {
            $data[] = $location;
        }

        $response->body( json_encode( $data ) );
    }
}
