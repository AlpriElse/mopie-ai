from sqlalchemy import create_engine

def create_connection(db_user, db_password, db_host, db_port, db_name):
  connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

  engine = create_engine(connection_string)

  return engine