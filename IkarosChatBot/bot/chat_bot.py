from time import time
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
from coffeehouse.exception import CoffeeHouseError as CFError
from IkarosChatBot.bot.errors import capture_err

from IkarosChatBot import app, LOGGER, CF_API_KEY, NAME
import IkarosChatBot.bot.database.IkarosChatBot_db as db


CoffeeHouseAPI = API(CF_API_KEY)
api_client = LydiaAI(CoffeeHouseAPI)


@app.on_message(~filters.me & filters.command('start', prefixes='/'), group=8)
@capture_err
async def start(_, message):
   if message.chat.type == "private":
     if len(message.text.split()) >= 2:
       suckz = message.text.split()[1]
       if suckz == "help":
          buttons =[
                        InlineKeyboardButton(
                             text="Updates Channel",
                             url="https://t.me/Techno_Ocean")
                     ]
          await message.reply_text('Machine Learning Chat Bot that can talk about any topic in any language. Powered by @Yuki_Network from @Techno_Ocean', reply_markup=InlineKeyboardMarkup(buttons))
     else:
       photo = "https://telegra.ph/file/19dad86d7b1009f1d6911.jpg"
       buttons =    
                        InlineKeyboardButton(
                             text="Updates Channel",
                             url="https://t.me/Techno_Ocean")
                     ]
       await message.reply_photo(photo,
         caption='Machine Learning Chat Bot that can talk about any topic in any language. Powered by @Yuki_Network from @Techno_Ocean',
         reply_markup=InlineKeyboardMarkup(buttons))
   else:
       await message.reply_text("Hi SweetHeart, I'm Ikaros.")


@app.on_message(filters.text & filters.group)
def IkarosChatBot_grp(client, message):
    msg = message
    if not check_message(client, msg):
        return
    user_id = msg.from_user.id

    if not user_id in db.USERS:
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        db.set_ses(user_id, ses_id, expires)

    sesh: str
    sesh, exp = db.get_ses(user_id)
    query = msg.text
    if int(exp) < time():
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        db.set_ses(user_id, ses_id, expires)
        sesh, exp = ses_id, expires
        
    try:
        app.send_chat_action(msg.chat.id, "typing")
        response = api_client.think_thought(sesh, query)
        msg.reply_text(response)
    except CFError as e:
        app.send_message(chat_id=msg.chat.id, text=f"An error occurred:\n`{e}`", parse_mode="md")


@app.on_message(filters.text & filters.private)
def IkarosChatBot_pvt(client, message):
    msg = message
    user_id = msg.from_user.id

    if not user_id in db.USERS:
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        db.set_ses(user_id, ses_id, expires)

    sesh: str
    sesh, exp = db.get_ses(user_id)
    query = msg.text
    if int(exp) < time():
        ses = api_client.create_session()
        ses_id = str(ses.id)
        expires = str(ses.expires)
        db.set_ses(user_id, ses_id, expires)
        sesh, exp = ses_id, expires

    try:
        app.send_chat_action(msg.chat.id, "typing")
        response = api_client.think_thought(sesh, query)
        msg.reply_text(response)
    except CFError as e:
        app.send_message(chat_id=msg.chat.id, text=f"An error occurred:\n`{e}`", parse_mode="md")
