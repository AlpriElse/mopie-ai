from dotenv import load_dotenv
import os
from sqlalchemy.orm import declarative_base
from mopie_data.db import create_connection
from mopie_data.video_metadata_entity import VideoMetadataEntity, Base

load_dotenv()

engine = create_connection()

Base.metadata.create_all(engine)
