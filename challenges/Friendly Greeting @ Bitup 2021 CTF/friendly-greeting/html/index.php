<?php

class FriendlyGreeting {
    public $param;
    public $file;

    public function __construct() {
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
        $page = new FriendlyGreeting;
        die($page->greet());
    } else {
        $page = new FriendlyGreeting;
        die($page->greet());
    }    
} else {
    // Debug-only purposes
    unserialize(base64_decode($_COOKIE['greeting']));
}

?>