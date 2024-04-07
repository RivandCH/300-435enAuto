from ncclient import manager
import xml.dom.minidom

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Change the hostname of a device
new_hostname = '''
                <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
                  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
                    <hostname>NetconfWasHere</hostname>
                  </native>
                </config>
            '''

with manager.connect(**cat_8kv) as m:
    # Retrieve the configuraiton
    results = m.edit_config(target='running', config=new_hostname)
    print(results)