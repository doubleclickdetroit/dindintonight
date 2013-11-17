<?php
require_once 'bootstrap.php';

$userRepository = $entityManager->getRepository('User');
$users = $userRepository->findAll();

foreach ($users as $user) {
    echo sprintf("- %s, %s\n", $user->getName(), $user->getFacebookId());
}
