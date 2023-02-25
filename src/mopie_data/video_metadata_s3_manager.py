import boto3
import json
from mopie_common.models import VideoMetadata
from itertools import chain

s3 = boto3.client('s3')

BUCKET_NAME='mopie-video-metadata'

class VideoMetadataS3Manager():

  def fetch_all_ids(self) -> [str]:
    paginator = s3.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=BUCKET_NAME)
    contents = chain.from_iterable(page['Contents'] for page in pages)

    keys = map(lambda obj: obj['Key'], contents)
    ids = map(lambda key: self._build_id_from_key(key), keys)

    return list(ids)


  def fetch_by_id(self, id: str) -> VideoMetadata:
    response = s3.get_object(
      Bucket=BUCKET_NAME, 
      Key=self._build_key_from_id(id)
    )

    metadata_json = response['Body'].read().decode('utf-8')

    return VideoMetadata.from_json(metadata_json)

  def _build_id_from_key(self, key: str) -> str:
    return key.replace(".info.json","")

  def _build_key_from_id(self, id: str) -> str: 
    return f'{id}.info.json'


