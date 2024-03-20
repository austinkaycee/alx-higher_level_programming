#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_state(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new State object to the session
        session.add(new_state)

        # Commit the transaction to the database
        session.commit()

        # Print the id of the new state
        print(new_state.id)

        # Close the session
        session.close()
