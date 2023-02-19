from db import create_connection
from dotenv import load_dotenv
import os
from sqlalchemy.orm import declarative_base
from video_metadata_entity import VideoMetadataEntity, Base

load_dotenv()

engine = create_connection(
  os.getenv('AWS_RDS_USER'), 
  os.getenv('AWS_RDS_PASSWORD'), 
  os.getenv('AWS_RDS_HOSTNAME'), 
  os.getenv('AWS_RDS_PORT'),
  os.getenv('AWS_RDS_DATABASE')
)

Base.metadata.create_all(engine)
