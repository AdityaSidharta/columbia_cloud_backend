import json
import base64
from io import BytesIO
from sagemaker.huggingface.model import HuggingFacePredictor
import datetime
import boto3
import os

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']

rekognition = boto3.client('rekognition')
predictor = HuggingFacePredictor(endpoint_name=ENDPOINT_NAME)
translate = boto3.client(service_name='translate')

def get_texts(response):
    textDetections=response['TextDetections']
    texts = []
    for text in textDetections:
        texts.append(text['DetectedText'])
    texts = ' '.join(texts)
    return texts

def lambda_handler(event, context):
    print("Received event : {}".format(event))

    current_datetime =  datetime.datetime.isoformat(datetime.datetime.now())
    print("current_datetime : {}".format(current_datetime))

    input_image = event['body']
    input_user_id = event['headers']['x-amz-meta-userid']
    input_language = event['headers']['x-amz-meta-language']
    print("input_image : {}".format(input_image))
    print("input_user_id : {}".format(input_user_id))
    print("input_language : {}".format(input_language))

    image = {'Bytes': BytesIO(base64.b64decode(input_image)).read()}
    response = rekognition.detect_text(Image=image)
    extracted_text = get_texts(response)
    print("extracted_text : {}".format(extracted_text))

    response = predictor.predict({
        'inputs': extracted_text
    })
    original_summary = response[0]['summary_text'].strip()
    print("original_summary : {}".format(original_summary))

    try:
        response = translate.translate_text(Text=original_summary, 
            SourceLanguageCode="en", TargetLanguageCode=input_language)
        summary = response.get('TranslatedText')
        summary_language = input_language
        print("summary : {}".format(summary))
    except:
        print("Language {} is not supported. Default to en".format(input_language))
        summary = original_summary
        summary_language = 'en'

    result = {
        'current_datetime': current_datetime,
        'extracted_text': extracted_text,
        'original_summary': original_summary,
        'summary': summary,
        'summary_language': summary_language,
        'input_user_id': input_user_id,
        'input_language': input_language,
    }
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps(result),
        "isBase64Encoded": False
    } 