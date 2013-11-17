<?php
require_once 'bootstrap.php';

$dropRepository = $entityManager->getRepository('Drop');
$drops = $dropRepository->findAll();

foreach ($drops as $drop) {
    var_dump( $drop );
}
