import requests, json

### Reserve the Meraki Sandbox for write access. Log in to meraki and create a new api-key
base_url = "https://api.meraki.com/api/v1"

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "1f4bcb02c69f8525384272e63fd93a450f41cfaa"
}

### Get the organization id for the sandbox. Store the value in a variable.
get_org_url ="/organizations"
org_id = requests.get(url=f"{base_url}{get_org_url}", headers=headers).json()[0]["id"]

### Get the id of our personal orgnetwork. Using a for loop looking for our personal orgnet name
get_orgnet_url = f"/organizations/{org_id}/networks"
org_nets = requests.get(url=f"{base_url}{get_orgnet_url}", headers=headers).json()
for org_net in org_nets:
    if org_net["name"] == "DNENT3-lxxxxxlhotmail.de":
        org_nets = org_net

### Change the networks timeZone
network_url = f"/networks/{org_nets["id"]}"

payload = {
    "timeZone" : "Europe/London"
}

change_timezone = requests.put(url=f"{base_url}{network_url}", data=json.dumps(payload), headers=headers).json()

print(f"""
We've started with the following Network-Settings:
TimeZone = {org_nets["timeZone"]}
I've changed the setting as follows:
TimeZone = {change_timezone["timeZone"]}
""")