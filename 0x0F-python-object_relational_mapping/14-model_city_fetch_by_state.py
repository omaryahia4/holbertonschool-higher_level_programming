#!/usr/bin/python3
""" lists all all City objects from the database hbtn_0e_14_usa"""


from model_city import City
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
    query_row = session.query(City, State).filter(City.state_id == State.id)\
                       .order_by(City.id).all()
    for City, State in query_row:
        print("{}: ({}) {}".format(State.name, City.id, City.name))
    session.commit
    session.close()
