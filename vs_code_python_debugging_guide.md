# How to Debug a Python API Script in VS Code
A simple guide to using **Step Over**, **Step Into**, **Step Out**, and **Continue** when debugging a Python script (example: Cisco SD‑WAN API).

---
## Prerequisites
- VS Code installed  
- Python extension installed  
- Your script saved (e.g., `sdwan_devices.py`)

---
## 1. Open the Script
1. Open VS Code  
2. Open the folder containing your Python file  
3. Select the correct Python interpreter  

---
## 2. Add a Breakpoint (Login Request)
Set a breakpoint on your login request:

```python
resp = session.post(login_url, data=payload, verify=False)
```

---
## 3. Start Debugging
- Press **F5**  
- Choose **Python File**

VS Code pauses at your breakpoint.

---
## 3.1 (Optional) Disable Debug Inline Values  
VS Code may show **yellow-highlighted inline variable values** during debugging.  
This feature is called **Debug Inline Values**.

If you want to disable it:

**Method 1 — Quick Toggle**  
1. Press **Ctrl + Shift + P**  
2. Search: **Toggle Inline Values**  
3. Turn it **OFF**

**Method 2 — Permanent Setting**  
Go to:

```
Settings → Debug → Inline Values
```

Uncheck:

```
Debug › Inline Values: Enabled
```

---
## 4. Step Over (F10) – Run the Line Without Entering Libraries
Press **F10** to run the login request.

Check in the Debug Console:

```python
resp.status_code
session.cookies
```

You should see:
- Status code `200`  
- A `JSESSIONID` cookie

---
## 5. Continue (F5)
Press **F5** to continue until the next breakpoint.

---
## 6. Add Breakpoint for Devices API
Add a breakpoint before retrieving devices:

```python
resp = session.get(devices_url, verify=False)
```

---
## 7. Step Over (F10)
Press **F10** to run the API call.

Check:

```python
resp.json()
```

---
## 8. Step Into (F11) – Enter Your Own Code
Break on your loop:

```python
for d in devices["data"]:
```

Press **F11** to go *into* the loop logic.

Try:

```python
d
```

---
## 9. Step Over (F10) – Process One Device
Step through each iteration:

```python
print(f"- {d['host-name']}, ({d['deviceId']})")
```

---
## 10. Step Out (Shift + F11)
Done inspecting the loop?  
Press **Shift + F11** to exit the function or loop.

---
## 11. Continue (F5) – Finish the Script
Press **F5** to complete execution.

---
## VS Code Debugger Controls

| **Action**     | **Shortcut** | **What It Does** |
|----------------|--------------|------------------|
| **Step Over**  | F10          | Runs the current line without entering any functions. |
| **Step Into**  | F11          | Enters the function being called. |
| **Step Out**   | Shift + F11  | Leaves the current function and returns to the caller. |
| **Continue**   | F5           | Runs until the next breakpoint or the program ends. |

---
