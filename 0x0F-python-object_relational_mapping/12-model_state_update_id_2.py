#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def change_state_name(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Query the State object with id = 2
        state_to_change = session.query(State).filter_by(id=2).first()

        # Change the name of the State object
        if state_to_change:
            state_to_change.name = "New Mexico"
            session.commit()
            print("State name changed successfully.")
        else:
            print("State with id 2 not found.")

        # Close the session
        session.close()
