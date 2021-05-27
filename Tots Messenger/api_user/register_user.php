<?php
$user = $_GET['user'];
$password = $_GET['pass'];
// Initialize the session
require_once("api_dbconnect.php");
// serialize the user inputs
$stmt = $link->prepare('INSERT INTO `users`(`user`, `pass`, `messages_sent`) VALUES (:usr, :pswd , 0)');
$stmt->execute(array(
    ':usr' => serialize($user),
    ':pswd' => serialize($password),
));
?>
