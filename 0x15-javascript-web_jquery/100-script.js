<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Header Color</title>
    <script>
        window.onload = function() {
            // Select the <header> element using document.querySelector
            const headerElement = document.querySelector('header');

            // Update the text color of the <header> element to red (#FF0000)
            headerElement.style.color = '#FF0000';
        };
    </script>
</head>
<body>
    <header>This is the header</header>
</body>
</html>

