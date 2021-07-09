import os
import telebot
from dotenv import load_dotenv

# loads .env file with token
load_dotenv()
# loads the API token
API_KEY = os.getenv('API_KEY')
# api = '1783277617:AAHbvpollk87oNBMIq6Ei20FC0OV3HqBpBs'
# Creates bot
bot = telebot.TeleBot(API_KEY)


# Handles messages to bot
@bot.message_handler(commands=['start'])
def greet(message):
    bot.reply_to(message, "Hey, How do you do? what can i help you with?\
                           /help - for help\
                           /contact - contact information of user\
                           /whatsapp - to get important updates from a a whatsapp group")


@bot.message_handler(commands=['help'])
def greet(message):
    bot.reply_to(message, "This bot seeks to help you get certain function\
                                       done and make some needed enquiries.")


@bot.message_handler(commands=['contact'])
def greet(message):
    bot.reply_to(message, "Maxwell Mawube\
                           024 XXX XXXX\
                           ahxxxxxxxxx@gmail.com")


@bot.message_handler(commands=['whatsapp'])
def greet(message):
    bot.reply_to(message, "Work is been done on the platform to serve your needs.")


# Searches/checks  for messages
bot.polling()

