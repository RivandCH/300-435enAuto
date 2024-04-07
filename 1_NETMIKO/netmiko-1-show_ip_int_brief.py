### Using the IOS XE Reservable Sandbox
from netmiko import Netmiko

cat_8kv = {
    "device_type": "cisco_xe",
    "ip": "10.10.20.48",
    "username": "developer",
    "password": "C1sco12345",
    "port": "22"
}

### Connect to the device using the dictionary defined above
con = Netmiko(**cat_8kv)

### Switch to enable-mode
con.enable()

### Send in commands
show_ip_int_brief = con.send_command("show ip int brief")
print(show_ip_int_brief)