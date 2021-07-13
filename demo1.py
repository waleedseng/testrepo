from netmiko import Netmiko

device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
    "fast_cli": False,
    "session_log": "test1.log",
}


net_connect = Netmiko(**device)
facts = net_connect.send_command(command_string="show version")
net_connect.disconnect()

print(facts)
