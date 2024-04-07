from ncclient import manager
import xmltodict, json

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Delete the interface
netconf_interface = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
            <name>Loopback987</name>
        </interface>
    </interfaces>
</config>"""

with manager.connect(**cat_8kv) as m:
    response = m.edit_config(target="running", config=netconf_interface)
    print(response)