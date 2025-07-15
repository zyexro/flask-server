from flask import Flask, request
import telegram

app = Flask(__name__)
bot = telegram.Bot(token="YOUR_BOT_TOKEN")

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(), bot)
    # معالجة الرسائل هنا
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
