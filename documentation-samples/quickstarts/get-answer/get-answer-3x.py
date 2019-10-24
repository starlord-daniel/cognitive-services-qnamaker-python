import requests
import json

# Represents the various elements used to create HTTP request URIs
# for QnA Maker operations.
# From Publish Page of the Qna Maker website
# Exact value of the host field
host = 'https://YOUR-RESOURCE-NAME.azurewebsites.net/qnamaker'

# Management APIs postpend the version to the route
# From Publish Page
# Example: /knowledgebases/ZZZ15f8c-d01b-4698-a2de-85b0dbf3358c/generateAnswer
# Is the exact value after POST
endpoint = '/knowledgebases/YOUR-KBID/generateAnswer'

# Authorization endpoint key
# From Publish Page
endpoint_key = "YOUR-ENDPOINT-KEY"

qna_url = host + endpoint

# The headers of the request to qna maker
# They don't need to be changed
headers = {
    "Authorization": f"EndpointKey {endpoint_key}",
    "Content-Type": "application/json"
}


def get_qna_response(question, qna_url, headers):
    '''
    This function returns the qna maker response to your question.
    '''
    data = {
        "question": question
    }

    try:
        # make a post call to the qna maker service
        response = requests.post(url=qna_url,
                                 data=json.dumps(data),
                                 headers=headers)
        return response.json()
    except Exception as e:
        # An exception occured - display it to the console
        print(e)


# Put your question here
question = "Is the QnA Maker Service free?"

# Get the answer from the function defined above
answer = get_qna_response(question, qna_url, headers)

# print the answer with indentation (which is more readable
print(json.dumps(answer, indent=4))
