from flask import Flask, request
import os
import telegram

app = Flask(__name__)

# استلام التوكن من متغيرات البيئة
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
bot = telegram.Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(), bot)
    # معالجة الرسائل هنا
    print("Received update:", update)
    return "OK"

if __name__ == '__main__':
    # تعيين Webhook تلقائيًا عند التشغيل
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    bot.set_webhook(url=WEBHOOK_URL)
    print(f"Webhook set to: {WEBHOOK_URL}")
    
    # تشغيل الخادم
    app.run(host='0.0.0.0', port=5000)
