# 🧠 LAN Hacking Simulator

**Author:** [Mr-A-Hacker](https://github.com/Mr-A-Hacker)  
**Project Type:** LAN-only forensic simulation  
**Tech Stack:** Flask + HTML + JS + SQLite (optional)  
**Status:** Active — educational use only

---

## 🎯 Purpose

This simulator is designed for ethical hacking education, forensic logging, and dramatic LAN-only demonstrations.  
It runs entirely offline and stores all data locally.  
No external calls. No real attacks. Just pure simulation.

---

## 🧩 Features

- ✅ IP logger (auto-triggered)
- ✅ Browser fingerprint module
- ✅ Battery status logger
- ✅ Location logger (with consent)
- ✅ Webcam consent logger (live video feed)
- ✅ Modular trigger routes (`/trigger/...`)
- ✅ Local log storage in `/logs/`
- ✅ Login → Consent → Dashboard flow
- ✅ Raspberry Pi compatible

---

## 🛠️ Setup

```bash
git clone https://github.com/Mr-A-Hacker/lan-hacking-simulator.git
cd lan-hacking-simulator
pip install flask
```

---

## 🚀 How to Start

```bash
# Run the Flask server on localhost
flask run --host=127.0.0.1 --port=5000
```

Then open your browser and go to:

```
http://localhost:5000
```

✅ All modules will run locally  
✅ Logs will be saved in the `/logs/` folder  
✅ No internet connection required

---

## 🧪 Modules

| Module     | Trigger Type     | Log File               | Notes                          |
|------------|------------------|------------------------|--------------------------------|
| IP         | Auto             | `logs/ip_log.txt`           | Logged on page load            |
| Fingerprint| Manual           | `logs/fingerprint_log.txt`  | Browser + OS + screen info     |
| Battery    | Auto             | `logs/battery_log.txt`      | Requires secure origin         |
| Location   | Button click     | `logs/location_log.txt`     | Requires user consent          |
| Webcam     | Button click     | `logs/webcam_log.txt`       | Logs consent only              |

---

## 🔐 Ethics

This project is strictly for educational and forensic simulation.  
It does **not** perform real attacks, scans, or data exfiltration.  
All modules are opt-in, consent-based, and LAN-only.

---

## 📸 Screenshots

> Add screenshots of:
> - `dashboard.html` (with trigger buttons)
> - `webcam.html` (live feed + consent)
> - `logs/` folder (sample entries)

---

## 🧠 Credits

Created by [Mr-A-Hacker](https://github.com/Mr-A-Hacker)  
Inspired by legacy, realism, and teachable moments.  
Built for Raspberry Pi, Ubuntu, and cross-platform LAN deployment.

---

## 📢 License

MIT License — free to fork, remix, and teach with attribution.

---

## 🔗 GitHub Profile

Explore more projects by Mr-A-Hacker:  
**[https://github.com/Mr-A-Hacker](https://github.com/Mr-A-Hacker)**
<img width="374" height="328" alt="5" src="https://github.com/user-attachments/assets/ea539925-edf1-4e43-bfaf-04e168354a97" />
