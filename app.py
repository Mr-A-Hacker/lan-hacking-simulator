from flask import Flask, render_template, request, redirect, session, jsonify
from modules import ip_logger, fingerprint, webcam
import os

app = Flask(__name__)
app.secret_key = 'legacy_sim_key'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/consent', methods=['POST'])
def consent():
    session['user'] = request.form['username']
    return render_template('consent.html')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    if 'accept' in request.form:
        return render_template('dashboard.html', user=session['user'])
    return redirect('/')

@app.route('/trigger/ip')
def trigger_ip():
    ip_logger.log(request)
    return "IP logged."

@app.route('/trigger/fingerprint')
def trigger_fingerprint():
    return fingerprint.capture(request)

@app.route('/trigger/webcam')
def trigger_webcam():
    consent = request.args.get('consent')
    webcam.consent_log(consent)
    return "Webcam consent logged."

@app.route('/webcam')
def webcam_page():
    return webcam.route()

@app.route('/trigger/battery', methods=['POST'])
def trigger_battery():
    data = request.get_json()
    with open('logs/battery_log.txt', 'a') as f:
        f.write(str(data) + '\n')
    return "Battery info logged."

@app.route('/trigger/location', methods=['POST'])
def trigger_location():
    data = request.get_json()
    with open('logs/location_log.txt', 'a') as f:
        f.write(str(data) + '\n')
    return "Location info logged."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
