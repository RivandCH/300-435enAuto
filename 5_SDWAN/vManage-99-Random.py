# Use the reservable sandbox for vmanage.
import requests, json, urllib3
urllib3.disable_warnings()

vmangage = "10.10.20.90"
base_url = f"https://{vmangage}"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Preparing the payload + endpoint URL to request the vManage Session Cookie
j_sec_url = f"{base_url}/j_security_check"
login_body = {
    "j_username": "admin",
    "j_password": "C1sco12345"
}

# Obtain the Cookie for vManage by sending in our username and password to the j_security_check API endpoint.
# If successfull: response.text = empty and in the response.header we find the Cookie
j_security_check = requests.post(url=j_sec_url, data=login_body, verify=False)
headers["Cookie"] = j_security_check.headers["set-cookie"].split(";")[0]

# Preparing the endpoint URL to request our X-XSRF-TOKEN. Sending the request and adding the token to our headers.
xsrf_url = f"{base_url}/dataservice/client/token"
xsrf_token = requests.get(url=xsrf_url, headers=headers, verify=False)
headers["X-XSRF-TOKEN"] = xsrf_token.text

###
# Administration API Stuff
###
""" 
# Get all users and their group membership
get_user_url = f"{base_url}/dataservice/admin/user"
get_users = requests.get(url=get_user_url, verify=False, headers=headers).json()["data"]

for user in get_users:
    print(f"{user["userName"]} is in all the following groups: {user["group"]}")


# Add a new user to our vManage.
create_user_url = f"{base_url}/dataservice/admin/user"
username = "myapiaccount"
new_user_body = {
    "group": ["basic"],
    "description": "just a random dude",
    "userName": username,
    "password": "highsecurepassword"
}

new_user = requests.post(url=create_user_url, headers=headers, verify=False, data=json.dumps(new_user_body))
print(new_user)
"""

###
# Device Inventory API Stuff
###
"""
# Get all connected devices
device_url = f"{base_url}/dataservice/device"
devices = requests.get(url=device_url, headers=headers, verify=False).json()["data"]

for device in devices:
    print(f"DeviceId: {device["deviceId"]} Device-Type:{device["device-type"]}")
"""
# Get all vEdges 39
vedge_url = f"{base_url}/dataservice/system/device/vedges"
vedges = requests.get(url=vedge_url, headers=headers, verify=False).json()["data"]

for vedge in vedges:
    print(f"{vedge["deviceType"]} with Serial {vedge["serialNumber"]}")
#print(json.dumps(vedges, indent=2))