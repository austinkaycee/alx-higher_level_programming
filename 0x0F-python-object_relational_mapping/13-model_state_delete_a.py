#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def delete_states_with_letter_a(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Query State objects containing the letter 'a'
        states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

        # Delete the State objects
        for state in states_to_delete:
            session.delete(state)

        # Commit the transaction to the database
        session.commit()
        print("States deleted successfully.")

        # Close the session
        session.close()
