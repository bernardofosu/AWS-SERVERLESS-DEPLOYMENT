To use curl to make a request to the API Gateway's invoke URL, follow this syntax:
Example curl command for a GET request:

curl https://uxc9vzn7t8.execute-api.us-east-1.amazonaws.com/prod

This will send a GET request to the endpoint and you should get a response with the student data, similar to what you saw in the logs.
Example curl command for a POST request with JSON data:

If you want to send data (e.g., for saving a student), you would do something like this:

curl -X POST https://uxc9vzn7t8.execute-api.us-east-1.amazonaws.com/prod \
-H "Content-Type: application/json" \
-d '{
  "studentid": "1",
  "name": "nana",
  "class": "Devops",
  "age": "27"
}'

Explanation:

    -X POST: Specifies that the request is a POST.

    -H "Content-Type: application/json": Sets the header to indicate that you're sending JSON data.

    -d: Sends the specified data in the body of the request.
