from ncclient import manager
import xmltodict, json

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Get Interface statistics of int GigEth0/1
int_filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>GigabitEthernet1</name>
    </interface>
  </interfaces-state>
</filter>
"""

with manager.connect(**cat_8kv) as m:
    netconf_response = m.get(int_filter)

### Print the data in a somewhat usable format
response_dict = xmltodict.parse(netconf_response.xml)
print(json.dumps(response_dict["rpc-reply"]["data"]["interfaces-state"]["interface"], indent=2))