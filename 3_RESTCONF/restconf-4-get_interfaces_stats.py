import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json"}
interfaces_url = 'ietf-interfaces:interfaces-state/'

# Get interface-state data of our device
interfaces = requests.get(url=f"{base_url}{interfaces_url}", auth=auth_cred, headers=headers, verify=False).json()["ietf-interfaces:interfaces-state"]["interface"]
print(json.dumps(interfaces, indent=2))

### Create some lines to differenciate the output
print("*" * 10)
print("*" * 10)
print("*" * 10)

# Get interface-state data of a single interface
interfaces_url = 'ietf-interfaces:interfaces-state/interface=GigabitEthernet1'
interfaces = requests.get(url=f"{base_url}{interfaces_url}", auth=auth_cred, headers=headers, verify=False).json()["ietf-interfaces:interface"]
print(json.dumps(interfaces, indent=2))