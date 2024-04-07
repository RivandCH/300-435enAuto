import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
hostname_url = 'Cisco-IOS-XE-native:native/hostname'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json"}

# Get Hostname of Device
response = requests.get(url=f"{base_url}{hostname_url}", auth=auth_cred, headers=headers, verify=False).json()
print(response)