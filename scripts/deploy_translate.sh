##!/bin/bash

rm -f translate.zip
rm -f function/lambda_function.py
cp lambda/translate.py function/
mv function/translate.py function/lambda_function.py
cd function
zip ../translate.zip lambda_function.py
cd ../package
zip -r ../translate.zip .
cd ../
aws s3 cp translate.zip s3://summit-lambda-functions/translate.zip --profile user1
rm -f function/lambda_function.py
touch function/lambda_function.py