<html style="background-image: url('img.jpg');">
    <?php
        require_once 'creds.php'; # Including user, pwd and flag variables
        if (isset($_POST[md5('login')]) && isset($_POST['username']) && isset($_POST['password'])) {
            if (strcmp($_POST['username'], sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(sha1(md5(md5(md5($user))))))))))))))))) == 0) { # Are you a crypto nerd?
                if (md5($_POST['password']) == sha1($pwd)) {
                    session_start();
                    if (isset($_SESSION['password'])) {
                        header("Location: manager.php");
                    } else {
                        $_SESSION['password'] = "oooooumama";
                        session_write_close();
                        sleep(2); # No bruteforce :)
                        session_start();
                        unset($_SESSION['password']);
                    }
                } else {
                    die("Hey h4x0r!");
                }
            } else {
                die("Bye h4x0r!");
            }
            # Secret AUTH
            if (md5($_POST['s3cr3t']) === sha1($pwd)) {
                echo $flag;
            }
        }
        if (isset($_GET['debug'])) {
            echo highlight_file(__FILE__, true);
        }
        if(isset($_POST['debug'])) { # Just for debugging
            echo var_dump($_SESSION);
            die();
        }        

    ?>

    <title>Mike's Dungeon</title>
    <h1 style="color: white;"><center>Mike's Dungeon</center></h1>
    <hr><br>

    <center>
        <form method="post" action="<?php basename($_SERVER['PHP_SELF']); ?>" name="signin-form">
            <div class="form-element">
                <label style="color: white;">Username -> </label>
                <input type="password" name="username" required />
            </div>
            <br>
            <div class="form-element">
                <label style="color: white;">Password -> </label>
                <input type="password" name="password" required />
            </div>
            <br>
            <button type="submit" name="login" value="login">Log In</button>
        </form>
    </center>

    <!-- Self-reminder: Dont forget to change your goals in your TXT file. -->

</html>