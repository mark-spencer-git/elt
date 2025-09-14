import elt
from sqlalchemy import text
import os

def transform(con):
    loc = os.path.join(os.path.dirname(elt.__file__), 'sql', 'sample.sql')
    with open(loc, 'r') as file:
        query = file.read()
        with con.connect() as connection:
            connection.execute(text(query))
            connection.commit()