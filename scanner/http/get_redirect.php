<?php

$url = $_POST['url'];

$headers = get_headers($url, 1);

$location = $headers['Location'];

$timeout = 0;

if (empty($location)) {
    echo "<li>No redirect detected.</li>";
} else if (is_array($location)) {
    echo "<h1>Redirect chain</h1>";
    echo "<ul>";
    foreach ($location as $l) {
        echo "<li><a href='$l'>$l</a></li>";
    }
    echo "</ul>";
} else {
    echo "<h1>Redirects to</h1>";
    echo "<a href='$location'>$location</a>";
}

