if ! [ -e "./mopie-transcription-lambda.zip" ]; then
  echo "mopie-transcription-lambda.zip not found. Run sh scripts/build-transcription-lambda.sh"
  exit 1
fi

aws lambda create-function \
  --function-name mopie-transcription-lambda \
  --runtime python3.8 \
  --handler mopie_transcription_lambda.lambda_handler \
  --role arn:aws:iam::118721456974:role/transcription-lambda-execution-role \
  --zip-file fileb://mopie-transcription-lambda.zip  \
  --timeout 60 \
  --memory-size 128