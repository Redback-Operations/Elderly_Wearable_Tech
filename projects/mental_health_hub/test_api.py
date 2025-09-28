import requests

#register
r = requests.post("http://127.0.0.1:5000/register", json={
    "username": "alice",
    "password": "mypassword"
})
print(r.json())

#login
r = requests.post("http://127.0.0.1:5000/login", json={
    "username": "alice",
    "password": "mypassword"
})
data = r.json()
print(data)

token = data.get("token")

#access protected route
r = requests.get("http://127.0.0.1:5000/protected", headers={
    "Authorization": f"Bearer {token}"
})
print(r.json())
