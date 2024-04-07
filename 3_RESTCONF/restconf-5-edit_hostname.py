import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
hostname_url = 'Cisco-IOS-XE-native:native/hostname'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json", "Content-Type": "application/yang-data+json"}

payload = json.dumps({"Cisco-IOS-XE-native:hostname": "AnotherRouter"})

# Returns an Errormessage, but it works. No idea why ^^
response = requests.put(url=f"{base_url}{hostname_url}", auth=auth_cred, data=payload, headers=headers, verify=False).json()
print(response)