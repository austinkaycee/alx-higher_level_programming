<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Translation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            function fetchTranslation() {
                // Get the language code entered by the user
                var languageCode = $('#language_code').val();

                // Fetch translation data from the API
                $.ajax({
                    url: 'https://www.fourtonfish.com/hellosalut/hello/',
                    method: 'GET',
                    data: { lang: languageCode },
                    success: function(response) {
                        // Update the text of the <div> element with ID 'hello' to display the translation
                        $('#hello').text(response.hello);
                    },
                    error: function() {
                        $('#hello').text('Error fetching translation');
                    }
                });
            }

            $('#btn_translate').click(fetchTranslation);

            $('#language_code').keypress(function(event) {
                // Check if the key pressed is Enter
                if (event.which == 13) {
                    // Prevent the default action (form submission)
                    event.preventDefault();
                    // Fetch translation when Enter is pressed
                    fetchTranslation();
                }
            });
        });
    </script>
</head>
<body>
    <input type="text" id="language_code" placeholder="Enter language code">
    <input type="button" id="btn_translate" value="Translate">
    <div id="hello"></div>
</body>
</html>

