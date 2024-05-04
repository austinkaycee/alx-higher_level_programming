// Fetch movie data from the URL using jQuery AJAX
$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function(response) {
        // Iterate over each movie in the response
        response.results.forEach(function(movie) {
            // Create a new <li> element with the movie title
            var listItem = $('<li>').text(movie.title);
            // Append the <li> element to the <ul> element with ID 'list_movies'
            $('#list_movies').append(listItem);
        });
    },
    error: function() {
        $('#list_movies').append($('<li>').text('Error fetching movie data'));
    }
});

