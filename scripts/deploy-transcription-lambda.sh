if ! [ -e "./mopie-transcription-lambda.zip" ]; then
  echo "mopie-transcription-lambda.zip not found. Run sh scripts/build-transcription-lambda.sh"
  exit 1
fi

aws lambda update-function-code \
  --function-name mopie-transcription-lambda \
  --zip-file fileb://mopie-transcription-lambda.zip  