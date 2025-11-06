from flask import render_template
from datetime import datetime

def consent_log(granted):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    status = "GRANTED" if granted == "true" else "DENIED"
    log_entry = f"[{timestamp}] Webcam consent: {status}\n"

    with open('logs/webcam_log.txt', 'a') as f:
        f.write(log_entry)

def route():
    return render_template('webcam.html')
