import os
from sqlalchemy import create_engine

def create_connection():
  _assert_env_vars_are_set()

  db_user = os.getenv('AWS_RDS_USER')
  db_password = os.getenv('AWS_RDS_PASSWORD') 
  db_host = os.getenv('AWS_RDS_HOSTNAME')
  db_port = os.getenv('AWS_RDS_PORT')
  db_name = os.getenv('AWS_RDS_DATABASE')

  connection_string = f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

  engine = create_engine(connection_string)

  return engine

def _assert_env_vars_are_set():
  assert os.getenv('AWS_RDS_USER') is not None
  assert os.getenv('AWS_RDS_PASSWORD') is not None
  assert os.getenv('AWS_RDS_HOSTNAME') is not None
  assert os.getenv('AWS_RDS_PORT') is not None
  assert os.getenv('AWS_RDS_DATABASE') is not None