from flask import jsonify
from datetime import datetime

def capture(request):
    data = {
        "timestamp": str(datetime.now()),
        "ip": request.remote_addr,
        "user_agent": request.headers.get('User-Agent'),
        "language": request.headers.get('Accept-Language'),
        "referer": request.headers.get('Referer'),
        "encoding": request.headers.get('Accept-Encoding'),
        "platform": request.user_agent.platform,
        "browser": request.user_agent.browser,
        "version": request.user_agent.version
    }

    log_entry = f"[{data['timestamp']}] IP: {data['ip']} | UA: {data['user_agent']} | Lang: {data['language']} | Platform: {data['platform']} | Browser: {data['browser']} {data['version']}\n"

    with open('logs/fingerprint_log.txt', 'a') as f:
        f.write(log_entry)

    return jsonify({"status": "captured", "data": data})
