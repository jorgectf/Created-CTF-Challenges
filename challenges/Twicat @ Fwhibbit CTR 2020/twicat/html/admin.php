<!DOCTYPE html>
<html>

<?php
ini_set('display_errors', 'off');
require_once 'hidden/data.php';

if (isset($_POST['submit']) && isset($_POST['username']) && isset($_POST['password'])) {
	if ( $_POST['username'] === $username && $_POST['password'] === $password) {
		session_start();
		$_SESSION['auth'] = "1";
		session_write_close();
	}
}

?>

<head>
	<title>TWICAT - Administrator Panel</title>
	<link rel="icon" type="image/jpg" href="twicat-favicon.jpg">
	<link rel="stylesheet" type="text/css" href="assets/css/bootstrap.min.css" media="screen">
	<link rel="stylesheet" type="text/css" href="assets/css/fontawesome/css/font-awesome.min.css" media="all" /> 
	<link rel="stylesheet" type="text/css" href="assets/css/application.css" media="screen">
	<script src="assets/js/jquery.js"></script>
	<script src="assets/js/bootstrap.min.js"></script>
</head>
<body>
	<div class="navbar navbar-fixed-top navbar-inverse" style='margin-top:-2px;'>
	  <div class="navbar-inner">
		<div class="container">
			<div class="nav-collapse collapse">
				<ul class="nav">
					<li class='active'><a class="brand" href="">TWICAT - Admin Panel</a></li>
				</ul>
				<ul class="nav pull-right">
					<li class='active' style='margin-top:2px;'><a href="<?php basename($_SERVER['PHP_SELF']); ?>" ><i class="icon-user"></i>&nbsp; Admin &nbsp; </a></li>
				</ul>
			</div>
		</div>
	  </div>
	</div>
	<style>body {
        background-color: #f5f5f5;
      }</style>
    
	<div class="container">
	<br>
	<div id="error" ></div>
	<div class="row">
		<div class="span4"></div>
		<?php session_start(); if (!isset($_SESSION['auth'])): ?>
			<center><h2>Administrator Login</h1><br>
			<div id="login">
				<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
				<h5>Username</h5>
				<input type="text" class="input-block-level" placeholder="Username" name="username" required>
				<h5>Password</h5>
				<input type="password" class="input-block-level" placeholder="Password" name="password" required>
				<input class="btn  btn-primary" type="submit" name='submit' value = "Submit" style='margin-top:10px;'/></center>
				</form>
			</div>
		<?php endif; session_write_close(); ?>
		<?php session_start(); if (isset($_SESSION['auth'])): ?>
			<center><h2>Administrator Panel</h1><br>
			<p>Here you have the available options to manage the server</p><br>
			<h4>Service Check</h4>
			<div id="login">
				<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
				<input class="btn  btn-primary" type="submit" name='db_check' value = "Check" style='margin-top:10px;'/>
				</form>
				<?php if (isset($_SESSION['auth']) && isset($_POST['db_check'])) { exec("netstat -antp", $out); echo "<pre>"; print_r($out); echo "</pre>"; } ?>
			</div>
			<br>
			<h4>Connectivity Check</h4>
			<div id="login">
				<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
				<input class="btn  btn-primary" type="submit" name='con_check' value = "Check" style='margin-top:10px;'/>
				</form>
				<?php if (isset($_SESSION['auth']) && isset($_POST['con_check'])) { exec("ping -c 1 8.8.8.8", $out); echo "<pre>"; print_r($out); echo "</pre>"; } ?>
			</div>
			<br>
			<h4>Post Check</h4>
			<div id="login">
				<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
				<input type="text" class="input-block-level" placeholder="Post URL" name="post_url" required>
				<input class="btn  btn-primary" type="submit" name='post_check' value = "Check" style='margin-top:10px;'/>
				</form>
				<?php if (isset($_SESSION['auth']) && isset($_POST['post_check'])) { exec(escapeshellcmd("curl " . escapeshellarg($_POST['post_url']) . " --output -"), $out); echo "<pre>"; print_r($out); echo "</pre>"; } ?>
			</div>
			<br>
		<?php endif; session_write_close(); ?>

		<br>
		<div class="span4"></div>
	</div>
	</div>
</body>
</html>
