<?php
$password = 0;
$user = 0;
// Initialize the session
require_once("api_dbconnect.php");
$user = $_GET['user'];
$password = $_GET['pass'];
$result = mysqli_query($link, "SELECT * FROM users WHERE user = '$user' AND pass = '$password'");
if($result->num_rows > 0) {
    echo'<p>accepted</p>';
    exit;
}
else {
    echo'<p>rejected</p>';
    exit;
}
?>