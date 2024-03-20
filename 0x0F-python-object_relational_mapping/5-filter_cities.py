#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys

def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)

        # Create a cursor object
        cursor = db.cursor()

        # Execute the SQL query with parameterized query to prevent SQL injection
        query = "SELECT cities.id, cities.name, states.name FROM cities \
                JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()
