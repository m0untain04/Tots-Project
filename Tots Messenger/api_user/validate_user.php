<?php
$user = $_GET['user'];
$password = $_GET['pass'];
// Initialize the session
require_once("api_dbconnect.php");
// serialize the user inputs
$stmt = $link->prepare('SELECT * FROM users WHERE user = :usr AND pass = :pswd');
$stmt->execute(array(
    ':usr' => serialize($user),
    ':pswd' => serialize($password),
));

if($stmt->num_rows > 0) {
    echo 'accepted';
    exit;
}
else {
    echo 'rejected';
    exit;
}
?>
