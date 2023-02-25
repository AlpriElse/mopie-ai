aws lambda invoke --function-name mopie-transcription-lambda \
  --cli-binary-format raw-in-base64-out \
  --payload file://mocks/event.json output.txt