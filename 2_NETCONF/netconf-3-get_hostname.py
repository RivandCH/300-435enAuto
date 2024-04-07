from ncclient import manager
import xml.dom.minidom

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Filter to get only the hostname of the device
FILTER = '''
                <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname></hostname>
                  </native>
                </filter>
            '''

with manager.connect(**cat_8kv) as m:
    # Retrieve the configuraiton
    results = m.get_config('running', FILTER)
    # Print the output in a readable format
    print(xml.dom.minidom.parseString(results.xml).toprettyxml())