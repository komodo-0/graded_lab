import json
import boto3

sqs = boto3.client('sqs')

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
            QueueUrl="https://sqs.us-east-1.amazonaws.com/515223095317/output_queue",
            MessageBody=json.dumps({"body": result})
        )

        return {
         'statusCode': 200,
         'body': result
         }

