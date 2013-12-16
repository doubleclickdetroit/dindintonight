<?php
namespace DinDin\DinDin\Controllers;

use Slim\Http\Request;
use Slim\Http\Response;

class Meals
{

    private $mealRepository;

    public function __construct( $mealRepository )
    {
        $this->mealRepository = $mealRepository;
    }

    public function __invoke( Request $request, Response $response, array $params, callable $notFound )
    {
        $data = array();

        foreach( $this->mealRepository->findAll() as $meal ) {
            $data[] = $meal;
        }

        $response->body( json_encode( $data ) );
    }
}
