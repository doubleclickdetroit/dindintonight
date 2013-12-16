<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class UsersId
{

    private $userRepository;

    public function __construct( $userRepository )
    {
        $this->userRepository = $userRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $id = $params['id'];

        $user = $this->userRepository->find( $id );

        if ( $user === null ) {
            call_user_func( $notFound );
            return;
        }

        $response->body( json_encode( $user ) );
    }
}
