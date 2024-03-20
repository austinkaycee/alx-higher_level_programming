#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def print_first_state(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Query the first State object
        first_state = session.query(State).order_by(State.id).first()

        # Display the result
        if first_state:
            print("{}: {}".format(first_state.id, first_state.name))
        else:
            print("Nothing")

        # Close the session
        session.close()
