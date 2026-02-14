# Cisco Catalyst SD-WAN Manager API in VS Code

## Structured Testing with `# %%`, Run Selection, and `if __name__ == "__main__"`

Using the Cisco DevNet SD-WAN Always-On Sandbox

------------------------------------------------------------------------

## 🎯 Goal

Login → Retrieve Device List → Print Hostnames & Device IDs

This guide demonstrates:

-   ✔ `# %%` cells for structured API testing\
-   ✔ Run Selection for quick validation\
-   ✔ `if __name__ == "__main__"` for professional script structure

------------------------------------------------------------------------

# 🧪 Example: Cisco SD-WAN Device Retrieval Script

Host:\
`https://sandbox-sdwan-2.cisco.com`

------------------------------------------------------------------------

``` python
# %%
# SECTION 1 - Authentication

import requests
import urllib3

# Ignore SSL warnings (sandbox uses self-signed cert)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = "https://sandbox-sdwan-2.cisco.com"
USERNAME = "devnetuser"
PASSWORD = "RG!_Yw919_83"

def login():
    """
    Authenticate and return a requests session
    with a valid JSESSIONID cookie.
    """
    session = requests.Session()
    login_url = f"{HOST}/j_security_check"

    payload = {
        "j_username": USERNAME,
        "j_password": PASSWORD
    }

    response = session.post(login_url, data=payload, verify=False)

    if response.status_code != 200 or "JSESSIONID" not in session.cookies:
        raise Exception("Login failed!")

    print("Logged in successfully")
    print("JSESSIONID:", session.cookies.get("JSESSIONID"))

    return session
```

------------------------------------------------------------------------

``` python
# %%
# SECTION 2 - Retrieve Devices

def get_devices(session):
    """
    Retrieve device list from SD-WAN Manager.
    """
    devices_url = f"{HOST}/dataservice/device"

    response = session.get(devices_url, verify=False)

    if response.status_code != 200:
        raise Exception(
            f"Failed to retrieve devices: {response.status_code}, {response.text}"
        )

    return response.json()
```

------------------------------------------------------------------------

``` python
# %%
# SECTION 3 - Main Execution

def main():
    print("Connecting to Cisco SD-WAN Manager...\n")

    session = login()
    devices = get_devices(session)

    print("Retrieved devices:\n")

    for device in devices.get("data", []):
        print(f"- {device['host-name']} ({device['deviceId']})")

if __name__ == "__main__":
    main()
```

------------------------------------------------------------------------

# 🎥 How to Demonstrate the 3 Techniques

------------------------------------------------------------------------

## 1️⃣ Using `# %%` Cells (Structured API Testing)

Run Section 1 only:

``` python
session = login()
session.cookies
```

Then test device retrieval:

``` python
devices = get_devices(session)
devices.keys()
```

Why this matters:

-   Validate authentication first\
-   Inspect JSON safely\
-   Avoid running the full script repeatedly

------------------------------------------------------------------------

## 2️⃣ Using Run Selection (Quick Validation)

Highlight and run:

``` python
len(devices["data"])
```

Or:

``` python
devices["data"][0]
```

Best for:

-   Checking device count\
-   Inspecting JSON structure\
-   Fast debugging

------------------------------------------------------------------------

## 3️⃣ Using `if __name__ == "__main__"` (Professional Structure)

``` python
if __name__ == "__main__":
    main()
```

This ensures:

-   Code runs only when executed directly\
-   Nothing runs automatically when imported\
-   Prevents accidental API execution

------------------------------------------------------------------------

# 🔥 Key Takeaway

When working with Cisco SD-WAN APIs:

-   Use cells for structured testing\
-   Use Run Selection for quick checks\
-   Always structure production automation with
    `if __name__ == "__main__"`

This is how professional network automation scripts should be built.
