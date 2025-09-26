# Logging Demo

## Overview
This project demonstrates a basic Python-based **logging and monitoring system**.  
It simulates user activity on a website, capturing events such as:

- Successful and failed logins  
- File uploads (with validation for safe extensions)  
- Chat messages (with spam detection and abuse flags)  
- Administrative log viewing and CSV export  

This was designed as a prototype to illustrate how user actions can be tracked for **security, auditing, and incident response**.

---

##  Requirements
- Python 3.8+  
- No external libraries required (uses only built-in modules: `datetime`, `random`, `csv`)  

---

##  Usage
Run the script from inside the `logging_demo` folder:


python activity_logger.py

Valid usernames: user_102, user_877, user_324, user_3424, admin342

Any password is accepted.

The admin342 account allows: Viewing all logs, Exporting logs to a .csv file

---

## Files

activity_logger.py - Python script implementing the logging system.

Logging & Monitoring.pdf - Documentation explaining the system design, features, and demonstration.

---

## Notes

File uploads accept only safe extensions (.png, .jpg, .jpeg, .pdf, .txt).

Sending 5+ chat messages in one session results in a spam flag and auto-logout.

Logs can be exported to CSV with dynamically generated headers for audit purposes.