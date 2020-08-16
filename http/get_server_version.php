<?php

$url = $_POST['url'];

$headers = get_headers($url, 1);

$server_version = $headers['Server'];

echo $server_version;
