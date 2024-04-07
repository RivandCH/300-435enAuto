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

### Get the device inventory of cisco dnac.
### Print the hostname and the serialNumber of each device.
get_devices_url = "intent/api/v1/network-device"
get_device_list = requests.get(url=f"{base_url}{get_devices_url}", headers=headers, verify=False).json()["response"]

for device in get_device_list:
    print(f"{device["hostname"]} has the SN {device["serialNumber"]}")
