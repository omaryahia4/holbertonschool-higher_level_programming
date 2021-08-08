#!/usr/bin/python3
""" delete all states that contains the
letter 'a' from the database hbtn_0e_6_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query_row = session.query(State).filter(State.name.like('%a%')).\
        delete(synchronize_session="fetch")
    session.commit()
    session.close()
