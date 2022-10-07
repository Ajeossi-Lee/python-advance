import requests
import json

# 获取token
url = "http://172.30.1.3:8989/api/token/login/"
headers = {'Content-Type':'application/json;charset=UTF-8'}
request_param = {
    "username":"test",
    "password":"limingzhu"
}
response = requests.post(url, data=json.dumps(request_param), headers=headers)
print(response.json()['auth_token'])
print(response.status_code)


# 验证token
# url = 'http://127.0.0.1:8000/api/v1/latest-products/'
# headers = {"Authorization": "Token 14133f0387b315bdd4e34dac5ca5aadcf98fd72d"}
# res = requests.get(url=url, headers=headers)
# print(res.text)
