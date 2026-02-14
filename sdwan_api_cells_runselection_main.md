# SD-WAN API Automation in VS Code: Structured Testing with Cells, Run Selection, and __main__

## Using #%% Cells, Run Selection, and if **name** == "**main**"

------------------------------------------------------------------------

## 🎯 Goal

Authenticate → Get Edges → Filter Online Edges → Print Their Names

This guide demonstrates:

-   ✔ `# %%` cells for structured API testing\
-   ✔ Run Selection for quick validation\
-   ✔ `if __name__ == "__main__"` for professional script structure

------------------------------------------------------------------------

## 🧪 Example SD-WAN API Script

``` python
# %%
# SECTION 1 - Authentication

import requests

API_HOST = "https://api.sdwan-controller.com"
TOKEN = "YOUR_API_TOKEN"

HEADERS = {
    "Authorization": f"Token {TOKEN}",
    "Content-Type": "application/json"
}

def get_edges():
    # Retrieve all SD-WAN edges from the controller
    url = f"{API_HOST}/api/sdwan/v2/enterprises/12345/edges"
    response = requests.get(url, headers=HEADERS)

    response.raise_for_status()
    return response.json()


# %%
# SECTION 2 - Filter Online Edges

def filter_online_edges(edges):
    # Return only edges with status == CONNECTED
    online = [
        edge for edge in edges
        if edge.get("edgeState") == "CONNECTED"
    ]
    return online


# %%
# SECTION 3 - Main Execution

def main():
    print("Retrieving edges from SD-WAN controller...\n")

    edges = get_edges()
    online_edges = filter_online_edges(edges)

    print(f"Total Edges: {len(edges)}")
    print(f"Online Edges: {len(online_edges)}\n")

    for edge in online_edges:
        print(f"{edge['name']} - {edge['edgeState']}")

if __name__ == "__main__":
    main()
```

------------------------------------------------------------------------

# 🎥 How to Demonstrate the 3 Techniques

------------------------------------------------------------------------

## 1️⃣ Using `# %%` Cells (Structured API Testing)

-   Run Section 1 only to test API retrieval.

-   Manually test:

    ``` python
    edges = get_edges()
    edges[0]
    ```

-   Run Section 2 separately to validate filtering logic.

Why this matters: - Validate raw API responses first - Debug JSON
structures safely - Avoid running the full script repeatedly

------------------------------------------------------------------------

## 2️⃣ Using Run Selection (Quick Validation)

Highlight and run:

``` python
len(edges)
```

Then:

``` python
len(filter_online_edges(edges))
```

Best for: - Checking edge counts - Validating logic quickly - Testing
small expressions without full execution

------------------------------------------------------------------------

## 3️⃣ Using `if __name__ == "__main__"` (Professional Structure)

``` python
if __name__ == "__main__":
    main()
```

This ensures: - The automation runs only when executed directly - The
script does NOT auto-run when imported - Prevents accidental API calls
or config pushes

Example:

``` python
from sdwan_script import get_edges
```

Notice nothing runs automatically.

------------------------------------------------------------------------

# 🔥 Key Takeaway

When working with SD-WAN APIs:

-   Use cells for structured testing\
-   Use Run Selection for quick checks\
-   Always structure production automation with
    `if __name__ == "__main__"`

This is how professional network automation scripts should be built.
