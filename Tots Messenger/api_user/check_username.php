<?php
$user = 0;
// Initialize the session
require_once("api_dbconnect.php");
$user = $_GET['user'];
$result = mysqli_query($link, "SELECT * FROM users WHERE user = '$user'");
if($result->num_rows > 0) {
    echo 'taken';
    exit;
}
else {
    echo 'valid';
    exit;
}
?>
