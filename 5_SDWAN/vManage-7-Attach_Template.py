### Code for SDWAN Reservable Sandbox
import requests, json, urllib3
from prettytable import PrettyTable
urllib3.disable_warnings()

base_url = "https://10.10.20.90"

### Getting our JSESSIONID Cookie from the header and parsing the string so we only have the cookie left.
auth_url = "/j_security_check"
auth_payload = {
    "j_username": "admin",
    "j_password": "C1sco12345"}

auth_response = requests.post(url=f"{base_url}{auth_url}", data=auth_payload, verify=False)
jsessionid = (auth_response.headers["Set-Cookie"].split(";")[0])

### Creating our Headers in preparation to get the XSRF-Token.
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Cookie": jsessionid}

### Retrieve the XSRF Token and add it to the header
token_url = "/dataservice/client/token"
headers["X-XSRF-TOKEN"] = token_response = requests.get(url=f"{base_url}{token_url}", headers=headers, verify=False).text

### Attach a template to a device
### Use the Show device template and get inventory scripts and hardcore these
template_url = "/dataservice/template/device/config/input"
payload = {
    "templateId": "e817727c-d53f-466b-af56-1a0bc659c54b",
    "deviceIds": ["C8K-8E7F818D-3379-3DD6-3556-19C322680AA5", "C8K-C9DF615F-ABE7-1573-2BB1-288797F1B78B"],
    "isEdited": False,
    "isMasterEdited": False
}
temp = requests.post(url=f"{base_url}{template_url}", headers=headers, data=json.dumps(payload), verify=False)
print(temp.status_code)