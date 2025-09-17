import urllib.request as rq
import json
import requests

# Peticion directa y sin dependencias externas
api_posts_url = "https://jsonplaceholder.typicode.com/posts"
# try:
#     response = rq.urlopen(api_posts_url)
#     data = response.read().decode("utf-8")
#     json_data = json.loads(data)
#     print(json_data)
#     response.close()
# except rq.HTTPDefaultErrorHandler as e:
#     print(f"HTTP Error: {e.code} - {e.reason}")

# utilizando el paquete requests
print('\nGET:')
respose = requests.get(api_posts_url)
print(respose.status_code)
print(respose.headers['Content-Type'])
print(respose.json()) 
data = respose.json()
print(data[0]['title'])

print('\nPOST:')
new_post = {
    "userId": 1,
    "title": "foo",
    "body": "bar"
}
response = requests.post(api_posts_url, json=new_post)
print(response.status_code)
print(response.json())


