<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>List Manipulation</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            // Add event listener for adding a new item
            $('#add_item').click(function() {
                // Create a new <li> element with the text "Item"
                var newItem = $('<li>').text('Item');
                // Append the new <li> element to the <ul> element with class my_list
                $('ul.my_list').append(newItem);
            });

            // Add event listener for removing the last item
            $('#remove_item').click(function() {
                // Remove the last <li> element from the <ul> element with class my_list
                $('ul.my_list li:last-child').remove();
            });

            // Add event listener for clearing the list
            $('#clear_list').click(function() {
                // Remove all <li> elements from the <ul> element with class my_list
                $('ul.my_list').empty();
            });
        });
    </script>
</head>
<body>
    <div id="add_item">Add Item</div>
    <div id="remove_item">Remove Item</div>
    <div id="clear_list">Clear List</div>
    <ul class="my_list">
        <!-- List items will be added dynamically here -->
    </ul>
</body>
</html>

