import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
capabilities_url = 'netconf-state/capabilities'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json"}

# Get the capabilities of our device
capabilities = requests.get(url=f"{base_url}{capabilities_url}", auth=auth_cred, headers=headers, verify=False).json()
for capability in capabilities['ietf-netconf-monitoring:capabilities']['capability']:
    print(capability)
    print(" ")
