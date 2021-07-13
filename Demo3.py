from netmiko import Netmiko
from pprint import pprint
from getpass import getpass


device = {
    "device_type": "cisco_xr",
    "ip": "10.48.32.89",
    "username": "iox",
    "password": getpass(),
    "port": 22,
    "fast_cli": False,
    "session_log": "test3.log",
    "conn_timeout": 15,
}


with Netmiko(**device) as net_connect:
    intfs = net_connect.send_command(command_string="show ip int br", use_textfsm=True)

pprint(intfs)
