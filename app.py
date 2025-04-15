from flask import Flask, request, send_file
import requests
import logging
from datetime import datetime
import os

app = Flask(__name__)

# Telegram bot settings
BOT_TOKEN = "8182919246:AAEqAvPr12ZFtJJQDHEl1pn5bfSZmMSb0PM"
CHAT_ID = "6684889364"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Set up logging
logging.basicConfig(filename="opens.log", level=logging.INFO)

def detect_device(user_agent):
    ua = user_agent.lower()
    if "iphone" in ua or "android" in ua or "mobile" in ua:
        return "📱 Mobile"
    elif "windows" in ua or "macintosh" in ua:
        return "💻 Desktop"
    else:
        return "❓ Unknown Device"

@app.route("/email-open")
def email_open():
    user_agent = request.headers.get("User-Agent", "N/A")
    ip_address = request.remote_addr
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    device_type = detect_device(user_agent)

    # Log to file
    log_msg = f"{timestamp} | IP: {ip_address} | Device: {device_type} | UA: {user_agent}"
    logging.info(log_msg)

    # Send Telegram notification
    message = (
        f"📬 Email Opened!\n"
        f"Time: {timestamp}\n"
        f"Device: {device_type}\n"
        f"IP: {ip_address}"
    )
    try:
        requests.post(TELEGRAM_API_URL, data={"chat_id": CHAT_ID, "text": message})
    except Exception as e:
        logging.error(f"Telegram error: {e}")

    # Return a transparent 1x1 GIF
    return send_file("pixel.gif", mimetype="image/gif")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))