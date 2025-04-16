from flask import Flask, request, send_file
import requests
from datetime import datetime

app = Flask(__name__)

seen_open_ips = set()

BOT_TOKEN = '8182919246:AAEqAvPr12ZFtJJQDHEl1pn5bfSZmMSb0PM'
CHAT_ID = '6684889364'

def send_telegram_alert(ip, user_agent):
    time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    message = f"📬 Email Opened!\nIP: {ip}\nTime: {time}\nBrowser: {user_agent[:60]}"
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": message})

@app.route('/email-open')
def email_open():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    user_agent = request.headers.get('User-Agent', 'unknown')

    if ip not in seen_open_ips:
        seen_open_ips.add(ip)
        send_telegram_alert(ip, user_agent)

    return send_file('tracker.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)