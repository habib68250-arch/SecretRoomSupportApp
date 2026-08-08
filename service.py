import telebot
import time

BOT_TOKEN = "8562006540:AAEOe54xtWK9FD5aXhx9PAEpmX5Ai2s8zDo"
GROUP_ID = -1003804414398

bot = telebot.TeleBot(BOT_TOKEN)

# User -> Group
@bot.message_handler(func=lambda m: m.chat.type == 'private')
def forward_to_group(message):
    text = f"📩 New Message\n👤 {message.from_user.first_name}\n🆔 {message.from_user.id}\n\n{message.text}"
    bot.send_message(GROUP_ID, text)

# Group reply -> User
@bot.message_handler(func=lambda m: m.chat.id == GROUP_ID and m.reply_to_message)
def reply_to_user(message):
    try:
        original = message.reply_to_message.text
        user_id = int(original.split("🆔 ")[1].split("\n")[0])
        bot.send_message(user_id, message.text)
    except Exception as e:
        print(e)

while True:
    try:
        bot.infinity_polling(skip_pending=True)
    except Exception as e:
        print(e)
        time.sleep(5)
