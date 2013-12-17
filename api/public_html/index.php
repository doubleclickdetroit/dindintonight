<?php

use Symfony\Component\Config\FileLocator;
use Symfony\Component\DependencyInjection\ParameterBag\ParameterBag;
use Symfony\Component\DependencyInjection\ContainerBuilder;
use Symfony\Component\DependencyInjection\Loader\YamlFileLoader;
use Symfony\Component\Yaml\Yaml;
use DinDin\DinDin\RouteLoader;

$root = implode( '/', array_slice( explode( '/', __DIR__), 0, -1 ) );

require $root . '/vendor/autoload.php';

$config = new ParameterBag( Yaml::parse( file_get_contents( $root . '/config/config.yml' ) ) ); 
$fileLocator = new FileLocator( $root . '/config' );

$dic = new ContainerBuilder( $config );
$dic->setParameter( 'root', $root );

$dil = new YamlFileLoader( $dic, $fileLocator );
$dil->load( 'di.yml' );

$slimConfig = $dic->getParameter('slim');

$app      = new \Slim\Slim( $slimConfig );

$dic->set( 'dic', $dic );

$dic->compile();

$routeLoader = new RouteLoader( $fileLocator, $app, $dic );
$routeLoader->load( 'routes.yml' );

$response = $app->response;
$response['Content-Type'] = 'application/json';


/*

// Locations //
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



 */

$app->run();
