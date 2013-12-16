<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class MealsId
{

    private $mealRepository;

    public function __construct( $mealRepository )
    {
        $this->mealRepository = $mealRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $id = $params['id'];

        $meal = $this->mealRepository->find( $id );

        if ( $meal === null ) {
            call_user_func( $notFound );
            return;
        }

        $response->body( json_encode( $meal ) );
    }
}
