// Fetch character data from the URL using jQuery AJAX
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    success: function(response) {
        // Update the text of the <div> element with ID 'character' to display the character name
        $('#character').text(response.name);
    },
    error: function() {
        $('#character').text('Error fetching character data');
    }
});

