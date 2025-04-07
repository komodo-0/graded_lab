import json
import boto3
import os

sqs = boto3.client('sqs')
output_queue_url = os.getenv("OUTPUT_QUEUE_URL")

def lambda_handler(event, context):
    for record in event["Records"]:
        body = json.loads(record["body"])

        number1 = float(body["number1"])
        number2 = float(body["number2"])
        operation = body["operation"]
        
        result = "Erreur. Veuillez choisir un opérateur parmi '+', '-', '*', '/'."

        if operation == "+":
            result = number1 + number2
        elif operation == "-":
            result = number1 - number2
        elif operation == "*":
            result = number1 * number2
        elif operation == "/":
            if number2 == 0:
                result = "Erreur: Division par zéro."
            else:
                result = number1 / number2
        
        sqs.send_message(
            QueueUrl= output_queue_url,
            MessageBody=json.dumps({"body": result})
        )

        return {
         'statusCode': 200,
         'body': "Succès"
         }

