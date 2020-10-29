<?php

require_once 'creds.php'; # Including user, pwd and flag variables
session_start();

if(!isset($_SESSION['password'])){
    header("Location: index.php?n1c3trY!");
    die();
} else {
    if(!isset($_GET[md5('letmein')])){
        $content = base64_encode(base64_encode(file_get_contents(basename($_SERVER['PHP_SELF']))));
        header("Location: index.php?Have_a_nice_day!$content");
        die();
    }  
}

# Secret Method
if (md5(sha1($_POST['s3cr3t'])) === sha1($pwd)) {
    echo $flag;
}

if(isset($_GET['debug'])) { # Just for debugging
    echo var_dump($_SESSION);
    die();
}

if(isset($_POST['yourinput']) && isset($_POST[sha1($_POST['yourinput'])])) {

    if(strpos($_POST['yourinput'], "/") !== false){
        die("What you trynna do¿?¿?");
    }

    $_POST['yourinput'] = strtolower($_POST['yourinput']);

    for($i = 0; $i < 300; ++$i) {
        $_POST['yourinput'] = preg_replace('/ph/', '', preg_replace('/ed/', '', preg_replace('/cr/', '', $_POST['yourinput'])));
    }

    $url = 'http://' . $_POST['yourinput'] . '.txt';

    $file = parse_url($url)[base64_decode("dXNlcg==")];
    $check = parse_url($url)[base64_decode("cGFzcw==")];

    if (empty($file)) {
        die("Get out of here!");
    } else {
        if (empty($check)) {
            die("Come and have a seat.");
        }
    }

    $_SESSION['info'] = base64_encode(file_get_contents($file));
    session_write_close();
    sleep(2); # Bye bye bruteforce
    sleep(0.337); # l33t
    session_start();
    unset($_SESSION['info']);

} else {
    die("Beep Boop!");
}

?>

<html style="background-image: url('img.jpg');">
    <title>SuperSecureVault</title>
    <h1 style="color: white;"><center>Mike's Manager doing management stuff</center></h1>
    <p1 style="color: white;"><center>Hi h4x0r, you are almost there! (Well, this is a self message as nobody will get here :P)<center></p1>
    <br><hr><br>

    <form method="post" action="<?php basename($_SERVER['PHP_SELF']); ?>" name="give me flagg">
        <div class="form-element">
            <label style="color: white;">What you wanna do?</label>
            <br><br>
            <input type="password" name="yourinput" required />
            <br><br>
        </div>
        <button type="submit" name="gooooooo" value="mikeisthebest">Log In</button>
    </form>
</html>
