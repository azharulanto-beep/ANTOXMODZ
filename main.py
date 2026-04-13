import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

PROJECTS = {
    "🔥 HG CHEATS": "https://www.mediafire.com/file/8gc3vh15uok2ugy/-WA0146.apks/file",
    "⚡ BR MODS": "https://brmods.net/download.php/apkroot",
    "💻 DRIP CLINT PC": "https://security.ezteam.net/downloads/DPLauncher(Aimkill).exe",
    "🚀 ANTO X CHEATS": "https://www.mediafire.com/file/t82yh1qsob0za5k/Flipkart_1.0.apk/file",
    "💎 ANTO PROJECT 1": "https://example.com/1",
    "💎 ANTO PROJECT 2": "https://example.com/2",
    "💎 ANTO PROJECT 3": "https://example.com/3",
    "💎 ANTO PROJECT 4": "https://example.com/4",
    "💎 ANTO PROJECT 5": "https://example.com/5",
    "💎 ANTO PROJECT 6": "https://example.com/6"
}

# সুন্দর Inline Button UI
def main_menu():
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = []

    for name in PROJECTS.keys():
        buttons.append(InlineKeyboardButton(name, callback_data=name))

    markup.add(*buttons)
    return markup


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "✨ *WELCOME TO ANTO PROJECT HUB* ✨\n\n👇 নিচ থেকে একটা সিলেক্ট কর:",
        parse_mode="Markdown",
        reply_markup=main_menu()
    )


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    name = call.data
    link = PROJECTS.get(name)

    if link:
        text = f"""
🔥 *{name}*

🚀 Download Now:
🔗 {link}

━━━━━━━━━━━━━━
⚡ Powered By ANTO
"""
        bot.send_message(call.message.chat.id, text, parse_mode="Markdown")


# Vercel Webhook
@app.route('/' + BOT_TOKEN, methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "ok", 200


@app.route('/')
def index():
    return "Bot Running ✅"
