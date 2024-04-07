import requests, json, urllib3
urllib3.disable_warnings()

base_url = 'https://10.10.20.48/restconf/data/'
interfaces_url = 'ietf-interfaces:interfaces/'
auth_cred= ("developer", "C1sco12345")
headers = {"Accept": "application/yang-data+json",
           "Content-Type": "application/yang-data+json"}

payload = {
    "ietf-interfaces:interface": {
            "name": "Loopback992",
            "description": "Restconf_interface992",
            "type": "iana-if-type:softwareLoopback",
            "enabled": True,
            "ietf-ip:ipv4": {
                "address": [
                    {
                    "ip": "10.19.49.22",
                    "netmask": "255.255.255.255"
                    }
            ]
        },
    }
}

# Create the new interface (Loopback 992) on the device
interface = requests.post(url=f"{base_url}{interfaces_url}", auth=auth_cred, data=json.dumps(payload),headers=headers, verify=False)
print(interface.status_code)
print(interface.text)

### Verify our Interface (Loopback 992) exists
response = requests.get(url=f"{base_url}{interfaces_url}interface=Loopback992", auth=auth_cred, headers=headers, verify=False).json()
print(json.dumps(response, indent=2))

### Delete the Interface (Loopback 992)
response = requests.delete(url=f"{base_url}{interfaces_url}interface=Loopback992", auth=auth_cred, headers=headers, verify=False)
print(response.status_code)
print("deleted.")

### Verify our Interface (Loopback 992) no longer exists
response = requests.get(url=f"{base_url}{interfaces_url}interface=Loopback992", auth=auth_cred, headers=headers, verify=False).json()
print(json.dumps(response, indent=2))