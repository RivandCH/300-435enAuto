import requests, json

### Runs for the Meraki always on sandbox
base_url = "https://api.meraki.com/api/v1"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

### Get the org id of "DevNet Sandbox"
get_org_url ="/organizations"
org_id = requests.get(url=f"{base_url}{get_org_url}", headers=headers).json()
for org in org_id:
    if org["name"] == "DevNet Sandbox":
        org_id = org["id"]

### Create a new network in our organization. Sadly returns 403 :/
network_url = f"/organizations/{org_id}/networks"
payload = {
    "name": "RivandNetwork",
    "productTypes": ["appliance", "switch"]
}

new_network = requests.post(url=f"{base_url}{network_url}", headers=headers, data=json.dumps(payload))
print(new_network.status_code)
print(new_network.text)
