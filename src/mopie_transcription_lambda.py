from mopie_common.models import TranscriptionTask

def lambda_handler(event, context):
  ids = []
  for record in event['Records']:
    payload = record["body"]
    
    transription_task = TranscriptionTask.from_json(payload)

    ids.append(transription_task.video_id)

  return ids