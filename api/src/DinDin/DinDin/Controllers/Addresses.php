<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class Addresses
{

    private $addressRepository;

    public function __construct( $addressRepository )
    {
        $this->addressRepository = $addressRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $data = array();

        foreach( $this->addressRepository->findAll() as $address ) {
            $data[] = $address;
        }

        $response->body( json_encode( $data ) );
    }
}
