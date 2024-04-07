from netmiko import Netmiko

router = {
    "host": "10.10.20.48",
    "port": 22,
    "username": "developer",
    "password": "C1sco12345",
    "device_type": "cisco_ios"}

### Simple configuration data to create a new loopback interface
configs = [
    "interface loop999",
    "ip address 10.99.99.99 255.255.255.0",
    "no shut"]

### Open a SSH connection using the previous specified variables.
### move into the enable state and then into the configure terminal state
### send in the config commands previously specified and create the interface
### Make sure the interface was created with the show command
with Netmiko(**router) as connection:
    connection.enable()
    connection.send_config_set(configs)
    print(connection.send_command("show ip int brief loop999"))