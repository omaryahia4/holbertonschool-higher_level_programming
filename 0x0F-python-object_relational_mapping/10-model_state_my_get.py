#!/usr/bin/python3
""" lists the state id of entered argument from the database hbtn_0e_6_usa"""


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
    query_row = session.query(State).filter_by(name=sys.argv[4]).first()
    if query_row is not None:
        print(query_row.id)
    else:
        print("Not found")
    session.close()
