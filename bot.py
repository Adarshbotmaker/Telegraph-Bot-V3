import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file
from Config import Config
psycho = Client(
    "Telegraph Uploader Bot",
    bot_token = Config.TOKEN,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")

START_TEXT = """
[!photo](https://telegra.ph/file/2af233c3b2db7aff4959b.jpg)
Heya I am Telegraph Media Converter🧳 
I can create Pictures under 5MB

~ If you face any problem in using this bot then please contact @adarshop_xd~
"""
HELP_TEXT = """
- Just give me a media under 5MB
- Then I will download it
- I will then upload it to the telegra.ph link

Support ~ @alpha_bot_support ~
"""
ABOUT_TEXT = """
- **Bot :** `Telegraph Uploader v3`
- **Python3 :** `3.9.6`
- **Updates Channel: **[Alpha x Updates](t.me/Alpha_bot_updates)
- **Support :** [Owner](t.me/adarshop_xd)

"""
START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Support', url="t.me/Best_Friends15"),
        InlineKeyboardButton('Updates', url='https://t.me/Master_X_Updates')
        ],
