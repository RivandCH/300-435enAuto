### Code for SDWAN Reservable Sandbox
import requests, json, urllib3
urllib3.disable_warnings()

base_url = "https://10.10.20.90"

### Getting our JSESSIONID Cookie from the header and parsing the string so we only have the cookie left.
auth_url = "/j_security_check"
auth_payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"}

auth_response = requests.post(url=f"{base_url}{auth_url}", data=auth_payload, verify=False)
jsessionid = (auth_response.headers["Set-Cookie"].split(";")[0])

### Creating our Headers in preparation to get the XSRF-Token.
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": jsessionid}

### Retrieve the XSRF Token and add it to the header
token_url = "/dataservice/client/token"
headers["X-XSRF-TOKEN"] = token_response = requests.get(url=f"{base_url}{token_url}", headers=headers, verify=False).text

### Create a new user
n_user_url = "/dataservice/admin/user"
create_payload = {
    "group": ["basic"],
    "description": "Best in Town",
    "userName": "createdwithapi",
    "password": "SecurePassword"
}

new_user = requests.post(url=f"{base_url}{n_user_url}", headers=headers, data=json.dumps(create_payload), verify=False)
if new_user.status_code == 200:
    print(f"New user {create_payload["userName"]} was created.")

### Change the password of the new user. Doesn't work. no idea why.
change_url = f"/dataservice/admin/user/password/{create_payload["userName"]}"
change_payload = {
    "userName": create_payload["userName"], 
    "password": "Default71"
}

change_pw = requests.put(url=f"{base_url}{change_url}", headers=headers, data=json.dumps(change_payload), verify=False)
print(change_pw)

### Get all Users and print them
list_user_url = "/dataservice/admin/user"
list_user = requests.get(url=f"{base_url}{list_user_url}", headers=headers, verify=False).json()["data"]
print("The following usersaccounts exist:")
for user in list_user:
    print(f"Username: {user['userName']}")

### Delete the created user again.
delete_url = f"/dataservice/admin/user/{create_payload['userName']}"
del_user = requests.delete(url=f"{base_url}{delete_url}", headers=headers, verify=False)
if del_user.status_code == 200:
    print(f"User {create_payload["userName"]} was deleted.")