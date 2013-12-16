<?php
use Doctrine\ORM\Tools\Setup;
use Doctrine\ORM\EntityManager;

require_once 'vendor/autoload.php';

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
