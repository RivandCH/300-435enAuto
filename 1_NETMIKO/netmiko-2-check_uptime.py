### Using the IOS XE Reservable Sandbox
from netmiko import Netmiko

### devices could be a list with many entries
devices = [{
    "device_type": "cisco_xe",
    "ip": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": "22"
}]

### Get the uptime of each device in our list.
for device in devices:
    net_connect = Netmiko(**device)
    output = net_connect.send_command("show version")
    net_connect.disconnect()

    ### Getting the data start
    result = output.find('uptime is')

    print(f"{device["ip"]} {output[int(result):int(result+20)]}")
