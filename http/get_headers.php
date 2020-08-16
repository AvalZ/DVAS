<?php

$url = $_POST['url'];

$headers = get_headers($url, 1);
print_r($headers);
