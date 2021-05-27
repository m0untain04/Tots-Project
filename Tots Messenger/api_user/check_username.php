<?php
$user = 0;
// Initialize the session
require_once("api_dbconnect.php");
$user = $_GET['user'];
$result = mysqli_query($link, "SELECT * FROM users WHERE user = '$user'");
if($result->num_rows > 0) {
    echo'<p>taken</p>';
    exit;
}
else {
    echo'<p>valid</p>';
    exit;
}
?>