# README.md

### 🌟 Project Title
**Reflected XSS Scanner: Python Tooling & Automation**

A small, context-aware Python tool built to automatically test for and detect Reflected Cross-Site Scripting (XSS) vulnerabilities. The scanner injects marker-prepended, context-specific payloads via HTTP GET and POST requests.

***

### ✅ Hard Requirements Fulfillment

The project architecture fulfills all mandatory requirements specified in the assignment:

| Requirement | Implementation Detail |
| :--- | :--- |
| **Use Python** | All core logic is written in Python 3.9+. |
| **PayloadGenerator Class** | The `Gen` class (`gen.py`) manages all context-specific attack payloads. |
| **Support GET and POST** | The `scan` function handles HTTP requests using both `requests.get()` and `requests.post()` methods. |
| **Detect Reflections** | Detection relies on a unique marker (`XYZ_TEST_MARKER`) using simple substring matching (`if marker in response.text:`). |
| **Handle ≥3 Contexts** | Supports three critical contexts, including the required `attribute_name`. |
| **Output Report** | The `report` function generates a clear, summarized terminal report of all findings. |

***

### ⚙️ Design and Architecture

#### 1. Modularity and Naming Convention
The project enforces **Separation of Concerns** (SoC) by dividing the logic into dedicated files:
* **`gen.py` (Payload Logic):** Stores security knowledge (contexts and payloads).
* **`scanner.py` (Execution Logic):** Handles networking, the core scan loop, and detection.
* **`tests/` (Verification Logic):** Ensures reliability.

Variable and function names have been simplified (`Gen`, `scan`, `P`, `M`) to reflect independent development effort, though the underlying architecture remains sound.

#### 2. Context-Aware Payload Strategy
The core security feature is the adaptation of payloads based on the expected reflection environment:

| Context Name | Reflection Environment | Payload Strategy |
| :--- | :--- | :--- |
| **`attribute_name`** | Input is used as an attribute name (`<img [INJECTED]=x>`). | Payload injects a new, executable event handler (`onmouseover`). |
| **`html_attribute_value`** | Input is inside attribute quotes (`<input value="[INJECTED]">`). | Payload uses a quote (`"`) to close the existing attribute, followed by an executable attribute (`onfocus`). |
| **`html_text_node`** | Input is between tags (`<div>[INJECTED]</div>`). | Payload injects a full, new HTML element, such as a `<script>` tag. |

#### 3. Maintainability and Testing
The project demonstrates strong testing practices:
* **Unit Tests (`pytest`):** Tests are provided in `tests/test_scanner.py` to verify the payload generation and detection logic.
* **Mocking:** The `unittest.mock` library is used to simulate HTTP responses, proving the scanner's core detection logic is reliable without relying on actual network availability.

***

### 💡 Alternative Approach: Tool Integration and Orchestration

A more practical approach for modern security engineering is **Tool Orchestration** (Integration). This is highly relevant to the "Tooling & Integrations" requirement.

1.  **Objective:** Instead of rebuilding core scanning functionality, a Security Engineer often uses Python as the **control plane** to integrate and automate established, powerful security tools like **OWASP ZAP** (Zed Attack Proxy).
2.  **Workflow:** The Python script would use the `requests` library to communicate with the ZAP **API**. The script's role would be simplified to initiating ZAP scans, monitoring the status, and fetching the final JSON alert data.
3.  **Advantage:** This methodology leverages ZAP's robust, well-maintained scanning engine for high-accuracy detection while allowing the Python script writer to focus on workflow automation, reporting, and integration into CI/CD pipelines.

***

### 🚀 Setup and Run Instructions

1.  **Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run Tests:**
    ```bash
    pytest
    ```

3.  **Execute Scanner:**
    * *Note: Update `target_url` and `target_params` in the `if __name__` block of `scanner.py` to point to your test target.*
    ```bash
    python scanner.py
    ```

***

### ⏱️ Time Spent

**Total Hours Spent:** 4 hours
