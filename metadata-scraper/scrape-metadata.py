import boto3
import os
import sys
from yt_dlp import YoutubeDL, DateRange

METADATA_OUTPUT_FOLER = 'metadata'

s3 = boto3.resource('s3')

def build_ydl_options(start_year, end_year):
  start_date = f'{start_year}0101'
  end_date = f'{end_year + 1}0101'

  return {
    'daterange': DateRange(start_date, end_date),
    'outtmpl': {
      'default': '%(id)s.%(ext)s'
    },
    'paths': {
      'home': METADATA_OUTPUT_FOLER
    },
    'writeinfojson': True,
    'skip_download': True,
  }

def main():
  """
  Usage:
  python3 scrape-metadata.py <youtube channel url> <start year> <end year>
  """
  youtube_channel_link = sys.argv[1]
  start_year = int(sys.argv[2])
  end_year = int(sys.argv[3])

  with YoutubeDL(build_ydl_options(start_year, end_year)) as ydl:
    ydl.download([youtube_channel_link])
 
  for filename in os.listdir(METADATA_OUTPUT_FOLER):
    s3.meta.client.upload_file(
      f'{METADATA_OUTPUT_FOLER}/{filename}', 
      'mopie-video-metadata', 
      filename
    )


if __name__ == "__main__":
    main()