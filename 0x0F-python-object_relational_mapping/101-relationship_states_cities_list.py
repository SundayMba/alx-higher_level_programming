#!/usr/bin/python3

"""
    module to list all state object from the database
"""

from relationship_state import State
from relationship_city import City, Base
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    # connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create the table
    Base.metadata.create_all(engine)
    # create a session with the connected database
    Session = sessionmaker(bind=engine)
    session = Session()

    # using the session, communicate with the database
    states = session.query(State)
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("{}: {}".format(city.id, city.name))
