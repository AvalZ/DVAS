<?php

$target = $_POST['target'];

echo '<pre>';
$stream = popen("/usr/bin/nmap -sV --top-ports 16 $target", 'r');

while (!feof($stream)) {

    //Make sure you use semicolon at the end of command
    $buffer = fread($stream, 1024);
    echo $buffer, PHP_EOL;

}

pclose($stream);
    
echo '</pre>';
