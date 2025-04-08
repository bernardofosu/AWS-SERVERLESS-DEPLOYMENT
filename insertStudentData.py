import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')

# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Extract values from the event object we got from the Lambda service and store in variables
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    # Write student data to the DynamoDB table and save the response in a variable
    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
    )
    
    # Return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }


import json
import boto3

# Create a DynamoDB object using the AWS SDK
dynamodb = boto3.resource('dynamodb')
# Use the DynamoDB object to select our table
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    # Log the event to confirm the structure
    print("Event received:", event)

    # Check for missing fields and return an error message if needed
    if 'studentid' not in event or 'name' not in event or 'class' not in event or 'age' not in event:
        return {
            'statusCode': 400,
            'body': json.dumps('Error: Missing required fields in the request.')
        }
    
    # Extract values from the event object we got from the Lambda service and store in variables
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    # Write student data to the DynamoDB table and save the response in a variable
    try:
        response = table.put_item(
            Item={
                'studentid': student_id,
                'name': name,
                'class': student_class,
                'age': age
            }
        )
        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps('Student data saved successfully!')
        }
    except Exception as e:
        # Handle DynamoDB exceptions
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error saving student data: {str(e)}')
        }
