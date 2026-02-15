import requests
import urllib3

# Ignore SSL warnings (self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# --- Configuration ---
HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

# --- Functions ---
def login():
    """Authenticate and return a session with JSESSIONID."""
    session = requests.Session()
    login_url = f"{HOST}/j_security_check"
    payload = {"j_username": USERNAME, "j_password": PASSWORD}
    response = session.post(login_url, data=payload, verify=False)

    if response.status_code != 200 or "JSESSIONID" not in session.cookies:
        raise Exception("Login failed!")
    print("Login successful. JSESSIONID obtained.")
    return session


def get_devices(session):
    """Retrieve devices from SD-WAN Manager."""
    devices_url = f"{HOST}/dataservice/device"
    response = session.get(devices_url, verify=False)

    if response.status_code != 200:
        raise Exception("Failed to retrieve devices")

    return response.json()


# --- Main (Production) ---
def main():
    session = login()
    devices = get_devices(session)

    for device in devices.get("data", []):
        print(f"{device['host-name']} ({device['deviceId']})")

if __name__ == "__main__":    
    main()
