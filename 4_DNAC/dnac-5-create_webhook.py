import requests, json, urllib3
urllib3.disable_warnings()

authentication = ("devnetuser", "Cisco123!")
base_url = "https://sandboxdnac2.cisco.com/dna/"
auth_url = "system/api/v1/auth/token"

headers = {
    "Accept":"application/json",
    "Content-Type":"application/json",
    "x-auth-token": requests.post(url=f"{base_url}{auth_url}", auth=authentication, verify=False).json()["Token"]}

### We want to create a subscription to an event using it's event id. We put ALL event-id's in a list.
assurance_url = "intent/api/v1/events?tags=ASSURANCE"
get_events = requests.get(url=f"{base_url}{assurance_url}", headers=headers, verify=False).json()
assurance_events = [event["eventId"] for event in get_events]

### Create the payload to create the subscription to the events.
payload = [{
    "name": "My Subscription",
    "subscriptionEndpoints": [{
        "subscriptionDetails":{
            "connectorType": "REST",
            "name": "My Reciever",
            "description": "Created using an API",
            "method": "Post",
            "url": "https://MyAzure.com/webhookdata"}
    }],
    "filter": {
        "eventIds": assurance_events}
}]

subscr_url = "intent/api/v1/event/subscription"
event_response = requests.post(url=f"{base_url}{subscr_url}", headers=headers, data=json.dumps(payload), verify=False)
print(event_response)