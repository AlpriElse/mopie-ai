from models import VideoMetadata
from mopie_data.video_metadata_entity import VideoMetadataEntity

class VideoMetadataAdapter:
  def __init__(self, video_metadata: VideoMetadata):
    self.video_metadata = video_metadata

  def to_entity(self) -> VideoMetadataEntity:
    return VideoMetadataEntity(
      self.video_metadata.id,
      self.video_metadata.title,
      self.video_metadata.duration,
      self.video_metadata.view_count,
      self.video_metadata.upload_date_iso,
    )
