import os
import telebot
import time
from dotenv import load_dotenv

# loads .env file with token
load_dotenv()
# loads the API token
API_KEY = os.getenv('API_KEY')
# api = '1783277617:AAHbvpollk87oNBMIq6Ei20FC0OV3HqBpBs'
# Creates bot
bot = telebot.TeleBot(API_KEY)

# Function returns text with @
def find_at(texts):
    for text in texts:
        if '@' in text:
            return text

# Handles messages to bot
@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Hey, How do you do? what can i help you with?\
\n/help - for help\
\n/contact - contact information of user\
\n/whatsapp - to get important updates from a whatsapp group\
\nYou can enter a users' name to search for the person on IG. eg @maxxies")


@bot.message_handler(commands=['help'])
def greet(message):
    bot.reply_to(message, "This bot seeks to help you get certain function\
done and make some needed enquiries.")


@bot.message_handler(commands=['contact'])
def greet(message):
    bot.reply_to(message, "Maxwell Mawube\
\n024 XXX XXXX\
\nahxxxxxxxxx@gmail.com")


@bot.message_handler(commands=['whatsapp'])
def greet(message):
    bot.reply_to(message, "Work is been done on the platform to serve your needs.")


# Handles users input for search on IG
@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_answer(message):
    texts = message.text.split()
    at_text = find_at(texts)
    bot.reply_to(message, "https://instagram.com/{}".format(at_text[1:]))


# Since connections can be closed, this helps the bot to keeping searching for messages always
while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)


