import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
interfaces_url = 'ietf-interfaces:interfaces/'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json"}

# Get the interface configuration of our device
interfaces = requests.get(url=f"{base_url}{interfaces_url}", auth=auth_cred, headers=headers, verify=False).json()["ietf-interfaces:interfaces"]["interface"]
print(json.dumps(interfaces, indent=2))