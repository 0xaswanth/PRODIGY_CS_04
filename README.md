# PRODIGY_CS_04

# Task-04: Simple Keylogger  
**ProDigy Infotech Internship Project**

## 📝 Project Description
This project demonstrates how to build a **basic keylogger** using Python. The program listens for keyboard inputs and logs every keystroke into a file for review. This keylogger is intended strictly for **educational purposes** and **must only be used with explicit consent** from all users being monitored.

---

## ⚠️ Ethical Consideration
> This tool must **never** be used for malicious purposes or without the explicit permission of the user. Unauthorized keylogging is **illegal and unethical**.

---

## 📁 Features
- Logs all keystrokes (including special keys like Enter, Space, Backspace).
- Saves logs in a timestamped `.txt` file inside a `logs/` directory.
- Stops logging when the **Escape** key is pressed.

---

## 🛠️ Requirements
- Python 3.x
- [`pynput`](https://pypi.org/project/pynput/) library

Install required dependency:
```bash
pip install pynput
```

---

## 🚀 How to Run
1. Clone or download the repository.
2. Navigate to the directory containing the Python file.
3. Run the script using:
```bash
python keylogger.py
```
4. Press the **Escape** key (`Esc`) to stop the keylogger.
5. The output log file will be saved in the `logs/` folder.

---

## 📂 Output
- Log files are saved with the format: `KeyLog_YYYY-MM-DD_HH-MM-SS.txt`
- Example log entry:
```
Keylogger Log File
Session started: 2025-05-07 10:30:00

h
e
l
l
o
Key.space
w
o
r
l
d
```

---

## 👨‍⚖️ Disclaimer
This script is designed for **learning** and **demonstration** purposes only. Do not use it to monitor anyone's activity without proper authorization.

---

## 📧 Contact
For any queries related to the project, please contact your internship coordinator at **ProDigy Infotech**.
