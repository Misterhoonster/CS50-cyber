import requests

# send secret key over network
url = "http://localhost:8080/fetch"
payload = {"name": "INSERT NAME HERE"}

requests.get(url, params=payload)
