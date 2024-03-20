#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states_with_letter_a(username, password, database):
    try:
        # Create engine to connect to MySQL server
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database))

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        # Query State objects containing the letter 'a' and sort by id
        states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

        # Display the results
        for state in states:
            print("{}: {}".format(state.id, state.name))

        # Close the session
        session.close()

    except Exception as e:
        print("Error: {}".format(str(e)))
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states_with_letter_a(username, password, database)

