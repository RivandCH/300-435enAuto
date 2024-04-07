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

### Submit CLI Commands to specified device. In return we recieve a task_id from DNAC.
command_url = "intent/api/v1/network-device-poller/cli/read-request"
device_id = ["32446e0a-032b-4724-93e9-acbbab47371b"]
payload = {
    "commands": [
        "show version",
        "show ip interface brief"
    ],
    "deviceUuids": device_id}

cli_response = requests.post(url=f"{base_url}{command_url}", headers=headers, data=json.dumps(payload), verify=False).json()["response"]

### Get the file id from the Command Runner API call using the url for the task returned in cli_response
task_url = f"intent{cli_response["url"]}"
task_response = requests.get(url=f"{base_url}{task_url}", headers=headers, verify=False).json()["response"]

### With the task id, we could get the file id. I hardcoded it in this example.
### Download the file of our show commands
file_url = "intent/api/v1/file/13d744a7-dd84-4f3e-9a4c-cac9c7d0fa4c"
file_response = requests.get(url=f"{base_url}{file_url}", headers=headers, verify=False).json()
print(file_response)