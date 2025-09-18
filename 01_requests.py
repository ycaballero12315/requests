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

try:
    print('\nPATCH:')
    update_post = {
        "title": "foo updated"
    }
    post_id = 1
    response = requests.patch(f"{api_posts_url}/{post_id}", json=update_post)
    print(response.status_code)
    print(f"Elemento actualizado: {response.json()}")

except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")

print('\nPUT:')
try:
    updated_post = {
        "userId": 1,
        "title": "foo updated",
        "body": "bar updated"
    }
    post_id = 1
    response = requests.put(f"{api_posts_url}/{post_id}", json=updated_post)
    print(response.status_code)
    print(f"Elemento reemplazado: {response.json()}")   
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")  

print('\nDELETE:')
try:
    post_id = 1
    response = requests.delete(f'{api_posts_url}/{post_id}')
    print(response.status_code)
    if response.status_code == 200:
        print(f"Elemento con ID {post_id} eliminado.")
    else:
        print(f"Error al eliminar el elemento con ID {post_id}.")
except requests.exceptions.HTTPError as e:
    print(f'Http_Error:{e.response.status_code} - {e.response.reason}')


