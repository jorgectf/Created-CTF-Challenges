#!/usr/bin/python3

from telegram.ext import Updater, CommandHandler
from telegram.ext.dispatcher import run_async
import subprocess
from shellescape import quote
from time import sleep
import os

token = "your-token-here"
staff = [staff-ids-here]
current = []
banned = []

@run_async
def start(bot, update):
    fromid = update.message.chat_id
    if fromid in current:
        bot.send_message(chat_id = fromid, parse_mode = "markdown", text = 'Please wait a moment.')
    elif fromid in banned:
        pass
    else:
        current.append(fromid)
        nick = update.message.from_user["username"]
        mensaje = update.message.text
        if fromid in staff:
            bot.send_message(chat_id = fromid, parse_mode = "markdown", text = '*Welcome to the Blind Hacker Bot*\n\nSend me your website and I will be opening it to test for vulnerabilities for 10 seconds.\n`(Example) /scan URL`\n\n*STAFF*\n/banid CHAT-ID\n/unbanid CHAT-ID\n/banneds')
        else:
            bot.send_message(chat_id = fromid, parse_mode = "markdown", text = '*Welcome to the Blind Hacker Bot*\n\nSend me your website and I will be opening it to test for vulnerabilities for 10 seconds.\n`(Example) /scan URL`')
        current.remove(fromid)

@run_async
def scan(bot, update):
    fromid = update.message.chat_id
    if fromid in current:
        bot.send_message(chat_id = fromid, parse_mode = "markdown", text = 'The Blind Hacker is currently checking your website, please wait a moment.')
    elif fromid in banned:
        pass
    else:
        nick = update.message.from_user["username"]
        mensaje = update.message.text
        url = mensaje.split()[1]
        current.append(fromid)
        safe_url = quote(url)
        for chatid in staff:
            bot.send_message(chat_id = chatid, parse_mode = "markdown", text = f"`{nick}` con chat-id `{fromid}` ha enviado `{mensaje}`.")
        subprocess.call(["python3", "browser.py", safe_url])
        current.remove(fromid)

@run_async
def banid(bot, update):
    fromid = update.message.chat_id
    if fromid in staff:
        mensaje = update.message.text
        id_to_ban = mensaje.split()[1]
        banned.append(int(id_to_ban))
        bot.send_message(chat_id = fromid, parse_mode = "markdown", text = f"Baneado chat-id `{id_to_ban}`.")

@run_async
def unbanid(bot, update):
    fromid = update.message.chat_id
    if fromid in staff:
        mensaje = update.message.text
        id_to_ban = mensaje.split()[1]
        banned.remove(int(id_to_ban))
        bot.send_message(chat_id = fromid, parse_mode = "markdown", text = f"Desbaneado chat-id `{id_to_ban}`.")

@run_async
def banneds(bot, update):
    fromid = update.message.chat_id
    if fromid in staff:
        bot.send_message(chat_id = fromid, parse_mode = "markdown", text = f"Baneado chat-id `{banned}`.")


updater = Updater(token, workers=25)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('scan', scan))
dispatcher.add_handler(CommandHandler('banid', banid))
dispatcher.add_handler(CommandHandler('unbanid', unbanid))
dispatcher.add_handler(CommandHandler('banneds', banneds))
updater.start_polling()
print("Bot started.")
updater.idle()