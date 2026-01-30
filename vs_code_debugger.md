# Debugging a Python API Script in VS Code  
## Using Step Over, Step Into, Step Out, and Continue

This guide demonstrates how to use VS Code’s debugger controls using a real-world
Cisco Catalyst SD-WAN Manager API Python script.

---

## Prerequisites
- VS Code installed
- Python extension (by Microsoft) installed
- Python file saved (example: `sdwan_devices.py`)

---

## Step 1: Open the Script in VS Code
1. Open VS Code
2. Open the folder containing `sdwan_devices.py`
3. Make sure the correct Python interpreter is selected

---

## Step 2: Add the First Breakpoint (Login Request)
Add a breakpoint on this line:

```python
resp = session.post(login_url, data=payload, verify=False)
```

This is where authentication happens.

---

## Step 3: Start Debugging
- Press **F5**
- Select **Python File**

Execution will pause at the breakpoint.

---

## Step 4: Use STEP OVER (F10) – Login Response Check
Press **F10 (Step Over)** to execute the login request.

You are stepping *over* the line without entering the `requests` library.

Now inspect values in the **Debug Console**:

```python
resp.status_code
session.cookies
```

Confirm:
- Status code is `200`
- `JSESSIONID` exists

---

## Step 5: Continue to the Next Section (F5)
Press **F5 (Continue)** to move forward until the next breakpoint
(or add one in the next step).

---

## Step 6: Add a Breakpoint for the Devices API Call
Add a breakpoint here:

```python
resp = session.get(devices_url, verify=False)
```

Execution pauses before retrieving the device list.

---

## Step 7: STEP OVER (F10) – Retrieve Devices
Press **F10 (Step Over)** to execute the API call.

Inspect in **Debug Console**:

```python
resp.status_code
resp.json()
```

This confirms the API response and JSON structure.

---

## Step 8: STEP INTO (F11) – Enter Your Own Code Logic
Add a breakpoint here:

```python
for d in devices["data"]:
```

Press **F5 (Continue)** until it hits.

Now press **F11 (Step Into)**.

You are stepping *into* the loop logic where each device is processed.

Inspect:

```python
d
d.keys()
```

This is useful for understanding each device object.

---

## Step 9: STEP OVER (F10) – Process One Device
While inside the loop, press **F10** to step through:

```python
print(f"- {d['host-name']}, ({d['deviceId']})")
```

Watch how `d` changes on each iteration.

---

## Step 10: STEP OUT (Shift + F11) – Exit the Loop
If you no longer need to inspect every device:

- Press **Shift + F11 (Step Out)**

VS Code runs the rest of the loop and exits back to the main script.

---

## Step 11: CONTINUE (F5) – Finish Execution
Press **F5 (Continue)** to let the script finish running.

Output will appear in the terminal.

---

## Summary of Debugger Controls Used

| Action        | Shortcut         | Purpose |
|--------------|------------------|--------|
| Step Over    | F10              | Run the next line without entering functions |
| Step Into    | F11              | Enter your own code or logic |
| Step Out     | Shift + F11      | Exit current function or loop |
| Continue     | F5               | Run until next breakpoint or program ends |

---

## Key Takeaways
- Use **Step Over** for API calls and libraries
- Use **Step Into** for your own logic
- Use **Step Out** when inspection is done
- Use **Continue** to move between breakpoints

This workflow is ideal for debugging API automation,
network monitoring scripts, and SD-WAN integrations.
