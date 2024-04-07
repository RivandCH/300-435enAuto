import requests, json, urllib3
urllib3.disable_warnings()

authentication = ("devnetuser", "Cisco123!")
base_url = "https://sandboxdnac.cisco.com/dna/"
auth_url = "system/api/v1/auth/token"
token = requests.post(url=f"{base_url}{auth_url}", auth=authentication, verify=False).json()["Token"]

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    "x-auth-token": token}

### Get all sites configured in dnac and print them with the name and id to the console
sites_url = "intent/api/v1/site"
get_sites = requests.get(url=f"{base_url}{sites_url}", headers=headers, verify=False).json()["response"]

for site in get_sites:
    print(f"{site["name"]} has the id {site["id"]}")

#print(json.dumps(get_sites, indent=3))