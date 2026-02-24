import telebot
import os
from database import conn, cursor

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

def is_admin(chat_id, user_id):
    admins = bot.get_chat_administrators(chat_id)
    for admin in admins:
        if admin.user.id == user_id:
            return True
    return False

@bot.message_handler(commands=['protect_on'])
def protect_on(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return
    
    cursor.execute("INSERT OR REPLACE INTO groups (group_id, protection) VALUES (?,1)", (message.chat.id,))
    conn.commit()
    bot.reply_to(message, "🟢 Protection Enabled")

@bot.message_handler(commands=['protect_off'])
def protect_off(message):
    if not is_admin(message.chat.id, message.from_user…
