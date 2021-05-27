<?php
$password = 0;
$user = 0;
// Initialize the session
require_once("api_dbconnect.php");
$user = $_GET['user'];
$password = $_GET['pass'];
$result = mysqli_query($link, "INSERT INTO `users`(`user`, `pass`, `messages_sent`) VALUES ('$user','$password', '0')");
?>