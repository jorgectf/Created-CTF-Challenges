<?php

class WeirdGreeting {
    public $param;
    public $file;

    public function __construct() {
        $this->init();
    }

    public function __wakeup() {
        $this->init();
    }

    public function init() {
        $this->file = ""; // for __destruct()
        $this->param = $_GET['name']; // for greet()
    }

    public function greet() {
        return "Hello, $this->param!";
    }

    public function __destruct() {
        if (!empty($this->file)) {
            include($this->file);
        }
    }
}

if (empty($_COOKIE['greeting'])) {
    if (empty($_GET['name'])) {
        $_GET['name'] = "Guest";
        $page = new WeirdGreeting;
        die($page->greet());
    } else {
        $page = new WeirdGreeting;
        die($page->greet());
    }    
} else {
    // Protected
    $_COOKIE['greeting'] = base64_decode($_COOKIE['greeting']);
    foreach(["flag", ".log", "self"] as $str) {
        if (strpos($_COOKIE['greeting'], $str)) {
            die("Super hacker detected!");
        }
    }
    unserialize($_COOKIE['greeting']);
}
?>