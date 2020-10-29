<!DOCTYPE html>
<html>

<?php
ini_set('display_errors', 'off');

class TwiCats {
    public function doQuery($sql) {
        $pdo = new SQLite3('twicat.db', SQLITE3_OPEN_READONLY);
        $pattern ="/.*['\"].*OR.*/i";
        $user_match = preg_match($pattern, $sql);
        $chars_consec = preg_match('/(.)\\1{1}/', $sql);
        if($user_match+$chars_consec > 0)  {
            die("<h1><span style='color: red;'>SQLi detected.</span></h1>");
        }
        else {
            $securesql = implode (['order', 'union', 'by', 'from', 'group', 'select', 'insert', 'into', 'values'], '|');
            $sql = preg_replace ('/' . $securesql . '/i', '', $sql);
            $query = 'SELECT id,name FROM cats WHERE id=' . $sql . ' LIMIT 1';
            $getCats = $pdo->query($query);
            $cats = $getCats->fetchArray(SQLITE3_ASSOC);
            if ($cats) {
                return $cats;
            }
            return false;
        }
    }
}
if (isset($_POST['cat_id']) && isset($_POST['submit'])) {
    
    $cat = new TwiCats ();
    $catDetails = $cat->doQuery($_POST['cat_id']);
}

if (isset($_POST['name']) && isset($_POST['submit'])) {
	if(strpos($_POST['name'], "/") !== false){
		die("Sorry, you are not allowed to see this resource.");
	}
	$_POST['name'] = strtolower($_POST['name']);
	echo "<h1>Here you have your image -></h1><br>";
	echo base64_encode(file_get_contents($_POST['name']));
	die();
}


?>


<head>
	<title>TWICAT</title>
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
					<li class='active'><a class="brand" href="">TWICAT</a></li>
				</ul>
				<ul class="nav pull-right">
					<li class='active' style='margin-top:2px;'><a href="<?php basename($_SERVER['PHP_SELF']); ?>" ><i class="icon-user"></i>&nbsp; Login &nbsp; </a></li>
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
		<center><h2>Cat Details</h1><br>
		<div id="login">
			<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
			<center><h5>Cat ID</h5>
			<input type="text" class="input-block-level" placeholder="ID" name="cat_id" id="ID" required>
			<input class="btn  btn-primary" type="submit" name='submit' value = "Submit" style='margin-top:10px;'/></center>
			</form>
		</div>
		<br>
		<?php if (isset ($catDetails) && !empty ($catDetails)): ?>
			<div class="row">
				<p class="well"><strong>Username for given ID</strong>: <?php echo $catDetails['NAME']; ?> </p>
				<p class="well"><strong>Other User Details</strong>: <br />
					<?php 
					$keys = array_keys ($catDetails);
					$i = 0;

					foreach ($catDetails as $user) { 
						echo $keys[$i++] . ' -> ' . $user . "<br />";
					} 
					?> 
				</p>
			</div>
		<?php endif; ?>
		<hr><br>
		<center><h2>Image Viewer</h1><br>
		<div id="login">
			<form class="form-signin" action="<?php basename($_SERVER['PHP_SELF']); ?>" method="post" style="border:0px;">
			<h5>Image name</h5>
			<input type="text" class="input-block-level" placeholder="misifu.jpeg" name="name" id="name" required>
			<input class="btn  btn-primary" type="submit" name='submit' value ="Submit" style='margin-top:10px;'/></center>
			</form>
		</div>
		<div class="span4"></div>
	</div>
	</div>
</body>
</html>
