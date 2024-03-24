import requests

# print(requests.get("http://localhost:5000/view_profile/2").text)

print(requests.post("http://localhost:5000/login",json={
    "user_id":1,
    "pwd":123
}).text)
