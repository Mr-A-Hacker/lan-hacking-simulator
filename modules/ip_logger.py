from datetime import datetime

def log(request):
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    log_entry = f"[{timestamp}] IP: {ip} | User-Agent: {user_agent}\n"

    with open('logs/ip_log.txt', 'a') as f:
        f.write(log_entry)
