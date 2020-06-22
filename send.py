import requests
import json

headers = {
    'Content-Type': 'text/plain',
    'url': 'https://www.google.com/',
    'output_id': '12345'
}
url = "http://localhost:5000/qr"

# Send request
response = requests.post(url, headers=headers)

# Response
contents = response.json()

print('Response Status Code: {}'.format(response.status_code))
print(json.dumps(contents, indent=4, sort_keys=True))
