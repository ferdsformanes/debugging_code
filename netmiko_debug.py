# Breakpoint              → pause execution at this line
# Continue (F5)           → resume execution until the next breakpoint
# Step Into (F11)         → enter into functions to debug line by line
# Step Over (F10)         → execute the next line without entering functions
# Step Out (Shift+F11)    → exit the current function and return to the caller

from netmiko import ConnectHandler

device = {
    "device_type": "cisco_xr",
    "host": "sandbox-iosxr-1.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
}

def connect_device(device):
    return ConnectHandler(**device)

def get_version(connection):
    return connection.send_command("show version")

connection = connect_device(device)

output = get_version(connection)

connection.disconnect()

print(output)
