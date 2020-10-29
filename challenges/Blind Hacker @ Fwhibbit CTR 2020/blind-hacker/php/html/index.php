<?php

if (!isset($_GET['indextoken'])) {
    die("indextoken param not supplied.");
} else {
    require_once 'connectors/tokendb.php';
    $tokennow = $_GET['indextoken'];
    $query = $conn->prepare("SELECT token FROM indextokens WHERE token = ?");
    $query->bind_param('s', $tokennow);
    $query->execute();
    $res = $query->get_result();
    $conn->close();

    if (isset($res) && !$res->num_rows > 0) {
        die("Invalid token! Have you met token.php?");
    }
}

if (isset($_POST['username']) && isset($_POST['password'])) {

    if ($_POST['username'] === "betauser") {
        if ($_POST['password'] === 'letsputapass!') {
            die("index.php is deprecated, please go to the new forum located at blind_hacker_forum (hostname). At least you got a part of the flag ;)");
        } else {
            die(";)");
        }
    }

    require_once 'connectors/mysql.php';

    $user = $_POST['username'];
    $pwd = $_POST['password'];

    $sql = "SELECT username, email, password FROM userinfo WHERE username = '$user' AND password = '$pwd';";
    $result = $conn->query($sql);
    $conn->close();
}

?>

<html>

<h1> BLIND HACKER FORUM </h1>

<center>
        <form method="post" action="<?php basename($_SERVER['PHP_SELF']); ?>" name="signin-form">
            <div class="form-element">
                <label>Username: </label>
                <input type="text" name="username" id="username" required />
            </div>
            <br>
            <div class="form-element">
                <label>Password: </label>
                <input type="password" name="password" id="password" required />
            </div>
            <br>
            <button type="submit" name="login" value="login">Log In</button>
        </form>
</center>

<?php if (isset($result) && $result->num_rows > 0) : ?>
    <a href="https://tenor.com/view/jesus-jesus-walk-yass-jesus-gif-14042558"></a>
<?php endif; ?>
<?php if (isset($result) && !$result->num_rows > 0) : ?>
    <p>Invalid username, email or password...</p>
    <a href="https://tenor.com/view/negros-ataud-ataud-meme-negros-dance-coffin-squad-gif-16889809"></a>
<?php endif; ?>

</html>
