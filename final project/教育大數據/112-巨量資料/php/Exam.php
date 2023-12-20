<?php 
require_once("function/DBConnectionHandler.php");

$serverName = "140.127.74.201:9001";   // host,運行於XAMPP時使用localhost即可。
$userName   = "root";        // 資料庫之使用者名稱，XAMPP預設root
$password   = "root";            // 資料庫使用者密碼，XAMPP預設空
$db         = "bigdata";        // 欲連接的資料庫名稱

try {
    DBConnectionHandler::setConnection(
        $serverName,
        $userName,
        $password,
        $db
    );
    $connection = DBConnectionHandler::getConnection();
    echo "Connection successful!".'<br>';
}catch(PDOException $e) {
    echo " ERROR " . $sql . "<br>" . $e->getMessage();
}


//1-1
DBConnectionHandler::setConnection(
    $serverName,
    $userName,
    $password,
    $db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT COUNT(DISTINCT dp001_review_sn) AS result 
        FROM edu_bigdata_imp1 
        WHERE PseudoID =:ID";
        
$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID",39);  #let id be 39
$stmt->execute();
$r = $stmt->fetch(PDO::FETCH_ASSOC);
print_r($r);


//1-2
DBConnectionHandler::setConnection(
    $serverName,
    $userName,
    $password,
    $db
);
$connection = DBConnectionHandler::getConnection();


$sql = "SELECT COUNT(DISTINCT dp001_question_sn) AS result 
        FROM edu_bigdata_imp1 
        WHERE PseudoID =:ID AND dp001_question_sn != :VAL;";

$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID",39);
$stmt->bindValue(":VAL","NA"); #let val be na
$stmt->execute();
$r = $stmt->fetch(PDO::FETCH_ASSOC);
print_r($r);


//2-1
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT dp001_video_item_sn, COUNT(DISTINCT dp001_indicator) AS result
        FROM edu_bigdata_imp1
        WHERE PseudoID = :ID AND dp001_indicator IS NOT NULL
        GROUP BY dp001_video_item_sn";

$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID", 281);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//2-2
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT COUNT(*) AS result
        FROM edu_bigdata_imp1
        WHERE PseudoID = :ID AND dp001_prac_score_rate = :score_rate";

$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID", 281);
$stmt->bindValue(":score_rate", 100);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//3-1
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT COUNT(dp001_record_plus_view_action) AS result
        FROM edu_bigdata_imp1
        WHERE PseudoID = :ID AND dp001_record_plus_view_action = :record_view_action";

$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID", 71);
$stmt->bindValue(":record_view_action", "paused");
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//3-2
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT DISTINCT DATE(dp001_review_start_time), DATE(dp001_review_end_time)
        FROM edu_bigdata_imp1
        WHERE PseudoID = :ID
        GROUP BY dp001_review_start_time, dp001_review_end_time";

$stmt = $connection->prepare($sql);
$stmt->bindValue(":ID", 71);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//4-1
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT dp001_review_sn, COUNT(*) AS total_views
        FROM edu_bigdata_imp1
        GROUP BY dp001_review_sn
        ORDER BY total_views DESC
        LIMIT 1";

$stmt = $connection->prepare($sql);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//4-2
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT COUNT(*) AS total_records
        FROM edu_bigdata_imp1
        WHERE dp002_extensions_alignment = '十二年國民基本教育類'";

$stmt = $connection->prepare($sql);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//4-3
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT dp002_verb_display_zh_TW, COUNT(*) AS occurrence_count
        FROM edu_bigdata_imp1
        WHERE dp002_verb_display_zh_TW != 'NA'
        GROUP BY dp002_verb_display_zh_TW
        ORDER BY occurrence_count DESC
        LIMIT 3";

$stmt = $connection->prepare($sql);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);


//4-4
DBConnectionHandler::setConnection(
$serverName,
$userName,
$password,
$db
);
$connection = DBConnectionHandler::getConnection();

$sql = "SELECT COUNT(*) AS total_records
        FROM edu_bigdata_imp1
        WHERE dp002_extensions_alignment = '校園職業安全'";


$stmt = $connection->prepare($sql);
$stmt->execute();
$result = $stmt->fetchAll(PDO::FETCH_ASSOC);

print_r($result);
?>