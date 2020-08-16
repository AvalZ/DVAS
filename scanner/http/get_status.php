<?php

$url = $_POST['url'];

$preamble = get_headers($url, 1)[0];

$exploded_preamble = explode(' ', $preamble, 3);

$version = $exploded_preamble[0];
$status_code = (int)$exploded_preamble[1];
$status_message = $exploded_preamble[2];

echo "Server status: $status_code $status_message";
