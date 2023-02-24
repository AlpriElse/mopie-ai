from mopie_data.video_metadata_entity import VideoMetadataEntity
from mopie_data.video_metadata_s3_manager import VideoMetadataS3Manager
from mopie_data.db import create_connection
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker
from adapters import VideoMetadataAdapter 
from models import VideoMetadata
from dotenv import load_dotenv

load_dotenv()

BATCH_SIZE = 100

engine = create_connection()
Session = sessionmaker(bind=engine)

def main(success_report_file, error_report_file):

  manager = VideoMetadataS3Manager()

  print('Fetching all ids...')
  ids = manager.fetch_all_ids()
  
  ids.sort()

  for i in range(0, len(ids) // BATCH_SIZE + 1):
    start_idx = i * BATCH_SIZE
    batch = ids[start_idx:start_idx + BATCH_SIZE]

    print(f" ===== Batch number {i}/{len(ids) // BATCH_SIZE} =====")
    print("Processing batch starting with", start_idx)

    print('Fetching all metadata...')
    def fetch_s3_metadata_as_obj(key):
      try:
        return manager.fetch_by_id(key)
      except TypeError as e:
        print(f'Error deserializing metadata with id {key}')
        error_report_file.write(f'{key}, deserialization error, {e}\n')
        return None
    all_video_metadatas = map(fetch_s3_metadata_as_obj, batch)
    all_video_metadatas = filter(lambda x: x != None, all_video_metadatas)
    
    print('Converting to entities...')
    all_entities = map(
      lambda meta: VideoMetadataAdapter(meta).to_entity(), all_video_metadatas
    )

    print('Writing to RDS...')

    session = Session()

    session.bulk_save_objects(
      all_entities
    )

    session.commit()
    session.close()

    success_report_file.write('\n'.join(batch))

if __name__ == '__main__':
  with open('success_report.txt', 'w') as success_report_file:
    with open('error_report.txt', 'w') as error_report_file:
      main(success_report_file, error_report_file)