import sys
from pyrogram import idle, Client
from IkarosChatBot import app, LOGGER

from IkarosChatBot.bot import chat_bot

if len(sys.argv) not in (1, 3, 4):
    quit(1)
else:
    app.start()
    LOGGER.info("Ikaros Is Up")
    idle()
