import os
from sqlalchemy import create_engine

# acknowledge that python not recommended for config file, however is current, working option
# to use environment variable for safe password storage (also allows comments)
db = {
    'server': 'postgresql+psycopg2',
    'user': 'postgres',
    'password': os.getenv('PG_KEY'),
    'port': '5432',
    'database': 'postgres'
}

# setting default - can change at runtime, editable install, future push for relative dir, etc.
source = os.path.join(os.getenv('HOME'), '/Documents/source_files')

class Connection:
    
    def __init__(self, server=db['server'], user=db['user'], password=db['password'], port=db['port'], database=db['database']):
        self.server = server
        self.user = user
        self.password = password
        self.port = port
        self.database = database
        self.con = create_engine(f"{self.server}://{self.user}:{self.password}@localhost:{self.port}/{self.database}")