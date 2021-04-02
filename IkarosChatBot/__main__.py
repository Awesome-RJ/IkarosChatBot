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

IKAROS_IMG= "https://telegra.ph/file/be7b7ec251dd14d7d2cd8.png"
IKAROSPINGIMG = "http://pa1.narvii.com/5734/0f0347710cef8bfcaf95528a61190b28cabe45a0_hq.gif"

else:
            first_name = update.effective_user.first_name
            update.effective_message.reply_photo(
                IKAROS_IMG,
                PM_START_TEXT.format(
                    escape_markdown(first_name),
                    escape_markdown(context.bot.first_name)),
                parse_mode=ParseMode.MARKDOWN,
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton(
                            text="Add Ikaros to your group",
                            url="t.me/{}?startgroup=true".format(
                                context.bot.username))
                    ],
                     [                         
                       InlineKeyboardButton(
                             text="Chat With Ikaros Lovers",
                             url="https://t.me/Hindi_K_Drama_1")
                     ],
                      [
                       InlineKeyboardButton(
                                text="Help",
                                url="t.me/{}?start=help".format(
                                    context.bot.username)
                     ],
                     [
                         InlineKeyboardButton(
                             text="Support Chat",
                             url=f"https://t.me/{SUPPORT_CHAT}"),
                  
                     ]]))
    else:
        update.effective_message.reply_video(
                IKAROSPINGIMG)
        update.effective_message.reply_text(
            "Ikaros! \n<b>ChatBot in command! since:</b> <code>{}</code>".format(uptime),
            parse_mode=ParseMode.HTML)