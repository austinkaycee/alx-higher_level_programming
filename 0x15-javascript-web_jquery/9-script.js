$(document).ready(function() {
    // Fetch translation data from the URL using jQuery AJAX
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        method: 'GET',
        success: function(response) {
            // Update the text of the <div> element with ID 'hello' to display the translation of "hello"
            $('#hello').text(response.hello);
        },
        error: function() {
            $('#hello').text('Error fetching translation');
        }
    });
});

