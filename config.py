import os
import telebot
from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
chat_id_str = os.getenv("CHAT_ID")

if bot_token is not None and chat_id_str is not None and chat_id_str.strip():
    try:
        bot = telebot.TeleBot(bot_token)
        chat_id = int(chat_id_str)
    except ValueError:
        print("Error: Invalid values for BOT_TOKEN or CHAT_ID.")
else:
    print("Error: BOT_TOKEN or CHAT_ID environment variables are not set or empty.")
