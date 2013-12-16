<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class Users
{

    private $userRepository;

    public function __construct( $userRepository )
    {
        $this->userRepository = $userRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $data = array();

        foreach( $this->userRepository->findAll() as $user ) {
            $data[] = $user;
        }

        $response->body( json_encode( $data ) );
    }
}
