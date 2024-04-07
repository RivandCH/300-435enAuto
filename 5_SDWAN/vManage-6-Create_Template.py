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

### Create a new device template, that contains a pre existing aaa feature template
template_url = "/dataservice/template/device/feature"
payload = {
    "templateName": "API2_created_Template_FORvmanage",
    "templateDescription": "Why would i ever use this",
    "deviceType": "vmanage",
    "configType": "template",
    "factoryDefault": False,
    "policyId": "",
    "featureTemplateUidRange":[],
    "generalTemplates": [
        {"templateId": "93374827-3ff5-4f36-94c6-43904516d9a4",
         "templateType": "aaa"}
    ]
}
temp = requests.post(url=f"{base_url}{template_url}", headers=headers, data=json.dumps(payload), verify=False)
print(temp.status_code)

### Use the show Device Template Script to see your template :)