import os
import telebot

API_KEY = "5550253771:AAGa-Zv0mGFqdE4WsSHXHrRF-5Vs-tafR8g"
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['stake'])
def stake(message):
  bot.reply_to(message,"You can stake your Elef World Tokens for Elef Gold at https://elefgold.com")

@bot.message_handler(commands=['buyelef'])
def buyelef(message): bot.send_message(message.chat.id,"You can buy Elef World Tokens at https://poocoin.app/tokens/0xb9ca307a74a6e4c114b3170b38c470c95b20f376")

def stake_request(message):
  request = message.text.split()
  if len(request) > 1 or request[0].lower() not in "stake":
    return False
  else:
    return True

@bot.message_handler(func=stake_request)
def stake(message):
  bot.reply_to(message,"You can stake your Elef World Tokens for Elef Gold at https://elefgold.com")

def buy_request(message):
  request = message.text.split()
  if len(request) > 1 or request[0].lower() not in "buy":
    return False
  else:
    return True

@bot.message_handler(func=buy_request)
def buyelef(message): bot.send_message(message.chat.id,"You can buy Elef World Tokens at https://poocoin.app/tokens/0xb9ca307a74a6e4c114b3170b38c470c95b20f376")

def info_request(message):
  request = message.text.split()
  if len(request) > 1 or request[0].lower() not in "info":
    return False
  else:
    return True

@bot.message_handler(func=info_request)
def infoelef(message): bot.send_message(message.chat.id,"Know more about ELEF WORLD TOKENS and our ELEF WORLD GAMES by visiting our website at https://www.elefworld.com/")

def updates_request(message):
  request = message.text.split()
  if len(request) > 1 or request[0].lower() not in "updates, update":
    return False
  else:
    return True

@bot.message_handler(func=updates_request)
def updateselef(message): bot.send_message(message.chat.id,"Watch updates about our progress on our YouTube page at https://www.youtube.com/channel/UCjfHD9_JAjiPA3nhmoMJURQ")

bot.polling()