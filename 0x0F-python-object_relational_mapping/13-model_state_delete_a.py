#!/usr/bin/python3

"""
    module to list all state object from the database
"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    # connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # create a session with the connected database
    Session = sessionmaker(bind=engine)
    session = Session()

    # using the session, communicate with the database
    states = session.query(State).order_by(State.id).filter(
            State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
    session.commit()
