from ncclient import manager

cat_8kv = {
    "host": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": 830,
    "hostkey_verify": False}

### Get all supported IETF YANG-Models
with manager.connect(**cat_8kv) as m:
    for capability in m.server_capabilities:
        if "interface" in capability:
            print(capability)