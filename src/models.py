from dataclasses import dataclass
import json

@dataclass(frozen=True)
class VideoMetadata:
  id: str
  title: str
  duration: int
  view_count: int
  upload_date_iso: str

  @classmethod
  def from_json(cls, json_str):
    data = json.loads(json_str)

    key_to_field = {
      'id': 'id',
      'title': 'title',
      'duration': 'duration',
      'view_count': 'view_count',
      'upload_date': 'upload_date_iso'
    }

    def object_hook(d):
      new_dict = {}
      for key, value in d.items():
        if key not in key_to_field:
          continue

        new_key = key_to_field.get(key, key)
        new_dict[new_key] = value
      return new_dict
    
    decoder = json.JSONDecoder(object_hook=object_hook)
    data = decoder.decode(json_str)

    return cls(**data)