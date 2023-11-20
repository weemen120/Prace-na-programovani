<!DOCTYPE html>
<html>
<head>
    <title>Webová stránka s tabulkou</title>
</head>
<body>

<h1>Tabulka s daty z databáze</h1>

<table border="1">
    <tr>
        <th>ID</th>
        <th>Jméno</th>
        <th>Příjmení</th>
        <th>Věk</th>
    </tr>

    <?php
    // Připojení k databázi
    $db_host = 'dbs.spskladno.cz';
    $db_user = 'student13';
    $db_password = 'spsnet';
    $db_name = 'vyuka13';

    $conn = new mysqli($db_host, $db_user, $db_password, $db_name);

    if ($conn->connect_error) {
        die("Chyba připojení k databázi: " . $conn->connect_error);
    }
    $mysqli->set_charset("utf8mb4")
    // SQL dotaz pro získání dat
    $sql = "SELECT * FROM HRY";

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            echo "<tr><td>" . $row["ID"] . "</td><td>" . $row["Jmeno"] . "</td><td>" . $row["Prijmeni"] . "</td><td>" . $row["Vek"] . "</td></tr>";
        }
    } else {
        echo "Nebyla nalezena žádná data.";
    }

    $conn->close();
    ?>
</table>

</body>
</html>