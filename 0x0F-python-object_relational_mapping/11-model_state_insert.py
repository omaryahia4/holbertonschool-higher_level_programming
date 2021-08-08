#!/usr/bin/python3
""" add new state "Louisiana" to the database hbtn_0e_6_usa"""


from typing import NewType
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
import model_state
from model_state import Base, State
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name="Louisiana")
    query_row = session.add(new)
    session.commit()
    print(new.id)
    session.close()
