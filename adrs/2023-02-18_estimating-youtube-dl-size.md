# Estimating Youtube-dl Size

MIT Opencourseware Youtube has ~6.9k Youtube Videos

_Storing Raw Video_
1 Hour of 1080p ~1 GB of data

Average video 30mins - 1 hour => 3.45 TB to 7 TB of video footage

_Storing only metadata_
Per video ~300KB

2.1 GB for all videos

_Storing Raw Audio_
1 Hour of audio ~64 MB (based off youtubedl `m4a/bestaudio/best`)

Assuming 6.9k videos are all ~1 hour long:

> 400 GB of audio data being stored

S3 Costs:
$0.023 per GB

~450 GB of audio --> $10.35/month for S3 storage costs
