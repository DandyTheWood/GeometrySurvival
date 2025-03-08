# About project
Geometry Survival is a game that I developed at the beginning of my journey into python game development using turtle library. It was one of my first projects, where I experimented with game mechanics, programming logic, and design.

# How to download and play:
## **1. Windows**
### **Step 1: Install Python**
1. Download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Run the installer and **check the box** that says **"Add Python to PATH"**.
3. Click **Install Now** and complete the installation.

### **Step 2: Verify Installation**
1. Open **Command Prompt** (`Win + R`, type `cmd`, and press Enter).
2. Type the following command and press **Enter**:
   ```sh
   python --version
   ```
   or
   ```sh
   python3 --version
   ```
   If Python is installed correctly, it will show the installed version.

### **Step 3: Run a Python Program**
- Navigate to the folder where your Python file (`script.py`) is located:
  ```sh
  cd path\to\your\file
  ```
- Run the Python script:
  ```sh
  python script.py
  ```
  or (if `python` does not work):
  ```sh
  python3 script.py
  ```

---

## **2. Linux**
### **Step 1: Install Python (If Not Installed)**
1. Open a terminal (`Ctrl + Alt + T`).
2. Check if Python is installed:
   ```sh
   python3 --version
   ```
3. If Python is not installed, install it using:
   ```sh
   sudo apt update   # For Debian/Ubuntu
   sudo apt install python3
   ```
   or
   ```sh
   sudo dnf install python3  # For Fedora
   sudo pacman -S python3     # For Arch Linux
   ```

### **Step 2: Run a Python Program**
- Navigate to the folder where your Python file (`script.py`) is stored:
  ```sh
  cd /path/to/your/file
  ```
- Run the script:
  ```sh
  python3 script.py
  ```

---

## **3. Mac**
### **Step 1: Install Python (If Not Installed)**
1. Open **Terminal** (`Cmd + Space`, type `Terminal`, and press Enter).
2. Check if Python is installed:
   ```sh
   python3 --version
   ```
3. If Python is not installed, install it using **Homebrew** (if not already installed):
   ```sh
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
   Then install Python:
   ```sh
   brew install python
   ```

### **Step 2: Run a Python Program**
- Navigate to the script location:
  ```sh
  cd /path/to/your/file
  ```
- Run the script:
  ```sh
  python3 script.py
  ```

