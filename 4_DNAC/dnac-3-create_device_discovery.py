import requests, json, urllib3
urllib3.disable_warnings()

authentication = ("devnetuser", "Cisco123!")
base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_url = "system/api/v1/auth/token"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    "x-auth-token": requests.post(url=f"{base_url}{auth_url}", auth=authentication, verify=False).json()["Token"]}

### Query for the credentials configured on dnac. We requiere the key "id" and later tell dnac to use the credentials with said "id"
cred_cli_url = "intent/api/v1/global-credential?credentialSubType=CLI"
cred_cli = requests.get(url=f"{base_url}{cred_cli_url}", headers=headers, verify=False).json()["response"][0]["id"]

### Create the device discovery using an IP Range. Requires a payload to be sent in.
### Not possible in sandbox. No Post Requests possible. Should work in theory ;)
payload = {
    "name": "MyFirstDiscoveryAPI",
    "discoveryType": "Range",
    "ipAddressList": "10.10.10.0-10.10.10.255",
    "timeout": 5,
    "protocolOrder": "ssh",
    "preferredMgmtIpMethod": "None",
    "globalCredentialList": [cred_cli]}

disc_url = "intent/api/v1/discovery"
disc_response = requests.post(url=f"{base_url}{disc_url}", headers=headers, data=json.dumps(payload), verify=False).json()
print(disc_response)