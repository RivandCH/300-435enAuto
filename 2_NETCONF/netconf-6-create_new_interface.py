from ncclient import manager
import xmltodict, json

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Create a Interface.
cisco_config = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback987</name>
            <description>CiscoWorks</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>true</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>192.168.111.111</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""

with manager.connect(**cat_8kv) as m:
    response = m.edit_config(target="running", config=cisco_config)
    print(response)