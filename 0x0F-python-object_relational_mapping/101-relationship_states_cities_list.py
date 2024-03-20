#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects contained in the database hbtn_0e_101_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

def list_states_and_cities(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Query all State objects with their corresponding City objects
        states = session.query(State).order_by(State.id).all()

        # Display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))
            for city in state.cities:
                print("\t{}: {}".format(city.id, city.name))

        # Close the session
        session.close()
