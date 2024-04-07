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

### Retrieve the templates and print them with useful information
template_url = "/dataservice/template/feature/"
templates = requests.get(url=f"{base_url}{template_url}", headers=headers, verify=False).json()["data"]

table = PrettyTable()
table.field_names = ["templateName", "templateId",]
for dev in templates:
    if "vedge-C8000V" in dev['deviceType']:
        table.add_row([dev['templateName'],dev['templateId']])
print(table)


"""
table = PrettyTable()
table.field_names = ["templateName", "templateId", "deviceType", "devicesAttached"]
for dev in templates:
    table.add_row([dev['templateName'],dev['templateId'],dev['deviceType'],dev['devicesAttached']])

print(table)
"""