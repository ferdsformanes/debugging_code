# How to Debug a Python API Script in VS Code

A simple guide to using **Step Over**, **Step Into**, **Step Out**, **Continue**, and **Watch expressions** when debugging a Python API script (example: Cisco SD-WAN Manager).

---

## Prerequisites
- VS Code installed  
- Python extension installed  
- Your script saved (e.g., `sdwan_devices.py`)  

---

## 1. Open the Script
1. Open VS Code  
2. Open the folder containing your Python file  
3. Select the correct Python interpreter (bottom-right of VS Code)

---

## 2. Add a Breakpoint (Login Request)
Set a breakpoint on the login request:

```python
resp = session.post(login_url, data=payload, verify=False)
```

This lets you verify authentication before moving forward.

---

## 3. Start Debugging
- Press **F5**  
- Choose **Python File**

VS Code pauses at your breakpoint.

---

## 3.1 (Optional) Disable Debug Inline Values
VS Code may show **yellow inline values** next to variables while debugging.

To disable:
```
Settings → Debug → Inline Values → Off
```

---

## 4. Step Over (F10) – Execute the Login Call
Press **F10** to run the login request.

Check values in the **Debug Console**:
```python
resp.status_code
session.cookies
session.cookies.get("JSESSIONID")
```

Expected:
- Status code: `200`
- A valid `JSESSIONID`

---

## 5. Continue (F5)
Press **F5** to run until the next breakpoint.

---

## 6. Add Breakpoint for Devices API Call
Add a breakpoint on the devices request:

```python
resp = session.get(devices_url, verify=False)
```

---

## 7. Step Over (F10) – Inspect API Response
Press **F10** to execute the request.

Check in the Debug Console:
```python
resp.status_code
resp.json().keys()
```

---

## 8. Add Breakpoint After JSON Parsing
Add a breakpoint after converting the response to JSON:

```python
devices = resp.json()
```

Inspect:
```python
type(devices)
len(devices["data"])
devices["data"][0]
```

---

## 9. Break on the Loop (First Iteration)
Add a breakpoint on the loop line:

```python
for d in devices["data"]:
```

Press **F11 (Step Into)** to enter the loop.

---

## 10. Step Over (F10) – Inspect One Device
Step to the print line:

```python
print(f"- {d['host-name']}, ({d['deviceId']}),({d['reachability']})")
```

At this point, `d` represents **one device**.

---

## 11. Add Watch Expressions
In the **Run and Debug → Watch** panel, add these expressions:

### Core device fields
```
d["host-name"]
d["deviceId"]
d["reachability"]
```

### Helpful extras
```
d["device-model"]
d["system-ip"]
d["site-id"]
```

### Defensive checks
```
d.get("host-name")
d.get("deviceId")
```

---

## 12. Optional: Conditional Breakpoints
Examples:

```python
d["reachability"] != "reachable"
```

```python
d["host-name"] == "vEdge-Cloud"
```

---

## 13. Step Through Devices
- **F10** → next device  
- Watch values update in real time  

---

## 14. Step Out (Shift + F11)
Press **Shift + F11** to exit the loop context.

---

## 15. Continue (F5)
Press **F5** to let the script complete.

---

## VS Code Debugger Controls

| Action | Shortcut | Description |
|------|----------|------------|
| Step Over | F10 | Run line without entering functions |
| Step Into | F11 | Enter loop or function |
| Step Out | Shift + F11 | Exit current function or loop |
| Continue | F5 | Run until next breakpoint |

---

### Debugging mindset
- Break after API calls  
- Inspect data shape once  
- Debug inside loops  
- Prefer Watch + conditional breakpoints  
