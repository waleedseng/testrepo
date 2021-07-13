from netmiko import Netmiko
from pprint import pprint

device = {
    "device_type": "cisco_ios",
    "ip": "sandbox-iosxe-latest-1.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 22,
    "fast_cli": False,
    "session_log": "test2.log",
}


with Netmiko(**device) as net_connect:
    facts = net_connect.send_command(command_string="show version", use_textfsm=True)

pprint(facts)
