<?php 

$serverName = "localhost";   // host,運行於XAMPP時使用localhost即可。
$userName   = "root";        // 資料庫之使用者名稱，XAMPP預設root
$password   = "";            // 資料庫使用者密碼，XAMPP預設空
$db         = "mydb";        // 欲連接的資料庫名稱

try {
    $connection = new PDO("mysql:host=$serverName;dbname=$db" , $userName , $password);
    $connection->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    echo "Connection successful!".'<br>';
}catch(PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}

?>