# Developer Fundamentals

## Environment Setup

### Installing Python on Windows

#### Step 1: Download Python
1. Go to the official Python website: [Python.org](https://www.python.org/)
2. Click on **Downloads** and select **Windows**.
3. Click on the latest **Python 3.x** version to download the installer.

#### Step 2: Install Python
1. Run the downloaded installer.
2. **Important:** Check the box **"Add Python to PATH"** before proceeding.
3. Click **Install Now** and follow the installation prompts.

#### Step 3: Verify Installation
1. Open the **Command Prompt** (Press `Win + R`, type `cmd`, and press Enter).
2. Type `python` and press Enter.
3. If Python is installed correctly, you should see a prompt like:
   ```
   Python 3.x.x (tags/v3.x.x) ...
   >>>
   ```
4. Type `exit()` and press Enter to exit Python.

#### Using PowerShell or Git Bash
- You can also use **PowerShell** (`Win + R`, type `powershell`, and press Enter) to run Python.
- If you want a Unix-like experience on Windows, install **Git Bash** from [Git for Windows](https://git-scm.com/download/win).

### Installing Python on macOS

#### Step 1: Check if Python is Preinstalled
1. Open **Terminal** (`Cmd + Space`, type "Terminal", and press Enter).
2. Type `python3 --version` and press Enter.
3. If Python 3 is installed, you will see output like:
   ```
   Python 3.x.x
   ```
   If Python 3 is not installed, proceed to the next step.

#### Step 2: Install Python
1. Go to [Python.org](https://www.python.org/)
2. Click on **Downloads** and select **macOS**.
3. Run the downloaded `.pkg` file and follow the installation steps.

#### Step 3: Verify Installation
1. Open **Terminal**.
2. Type `python3` and press Enter.
3. You should see the Python REPL (`>>>` prompt).
4. Type `exit()` to quit.

### Installing Python on Linux

#### Step 1: Check if Python is Installed
1. Open **Terminal** (`Ctrl + Alt + T`).
2. Type `python3 --version` and press Enter.
3. If Python 3 is installed, it will display the version number.

#### Step 2: Install Python (if not installed)
- **Ubuntu/Debian:**
  ```bash
  sudo apt update
  sudo apt install python3
  ```
- **Fedora:**
  ```bash
  sudo dnf install python3
  ```
- **Arch Linux:**
  ```bash
  sudo pacman -S python
  ```

#### Step 3: Verify Installation
1. Open **Terminal**.
2. Type `python3` and press Enter.
3. You should see the Python REPL (`>>>` prompt).
4. Type `exit()` to quit.

## Setting Up a Virtual Environment
Once Python is installed, it's best practice to use **virtual environments** for managing dependencies.

#### Creating a Virtual Environment
```bash
python3 -m venv myenv
```

#### Activating the Virtual Environment
- **Windows (Command Prompt):**
  ```
  myenv\Scripts\activate
  ```
- **Windows (PowerShell):**
  ```
  myenv\Scripts\Activate.ps1
  ```
- **macOS/Linux:**
  ```bash
  source myenv/bin/activate
  ```

#### Deactivating the Virtual Environment
```bash
deactivate
```

## Installing Developer Tools

### 1. Visual Studio Code (VS Code)
- Download from: [VS Code](https://code.visualstudio.com/)
- Install the **Python extension** from the Extensions Marketplace.
- Open a Python file and select the **Python interpreter** (Ctrl+Shift+P → "Python: Select Interpreter").

### 2. PyCharm
- Download from: [JetBrains PyCharm](https://www.jetbrains.com/pycharm/)
- Install and configure a Python interpreter.
- Supports **virtual environments** and **debugging tools**.

### 3. Jupyter Notebook
- Install Jupyter Notebook:
  ```bash
  pip install notebook
  ```
- Launch Jupyter Notebook:
  ```bash
  jupyter notebook
  ```
- Opens in your browser, allowing you to write and execute Python code interactively.

## Installing Packages with pip
To install packages, use `pip`:
```bash
pip install package_name
```
To install multiple packages from a file:
```bash
pip install -r requirements.txt
```

## Key Takeaway
> **Setting up your Python environment correctly ensures smooth development and avoids conflicts.**

Now you're ready to start coding in Python! 🚀