#!/usr/bin/python3
""" add new state "California" and new city "San francisco"
to the database hbtn_0e_6_usa"""


from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker
from relationship_state import Base, State
from relationship_city import Base, City
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="California")
    new_state.cities = City(name="San Francisco")
    query_row = session.add(new_state)
    session.commit()
    session.close()
