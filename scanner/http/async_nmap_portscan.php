<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <pre id='scan-results'>
Scanning <?php echo $_POST['target']; ?>...
    </pre>
    <script>
        var scanres = document.getElementById("scan-results");

        fetch('/http/nmap_portscan.php', {
            "headers": { "Content-Type": "application/x-www-form-urlencoded" },
            "body": "target=<?php echo $_POST['target']; ?>",
            "method": "POST"
        }).then(function (response) {
            return response.text();
        }).then(function (html) {
            scanres.innerHTML = html;
        }).catch(function (err) {
            scanres.innerHTML = 'Something went wrong';
        });

    </script>
</body>
</html>
