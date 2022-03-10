import sys
from pyrogram import idle, Client
from IkarosChatBot import app, LOGGER

from IkarosChatBot.bot import chat_bot

if len(sys.argv) in {1, 3, 4}:
    app.start()
    LOGGER.info("Ikaros Is Up")
    idle()

else:
    quit(1)
