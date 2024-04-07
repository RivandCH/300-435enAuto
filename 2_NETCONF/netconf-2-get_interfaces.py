from ncclient import manager
import xml.dom.minidom

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Get data about the configured interfaces. Using xml.dom.minidom for nice formatting.
filter = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
        <name/>
        <enabled/>
        <description/>
    </interface>
  </interfaces>
</filter>
"""

with manager.connect(**cat_8kv) as m:
    interfaces = m.get_config('running', filter)
    print(xml.dom.minidom.parseString(interfaces.xml).toprettyxml())