from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import os  
from os import environ

# Replace 'my_account' with your own API ID and API Hash
app = Client("my_account", api_id="12293838", api_hash="cf8c7db0d609148786e7ca5c706909bd")

# Define the introductory text
INTRO_TEXT = "Welcome! Click on the buttons below to join our channels."

@Client.on_message(filters.command("joinchannels"))
def join_channels(client, message):
    # Create inline keyboard buttons
    buttons = [
        [InlineKeyboardButton("Channel 1", url="https://t.me/Pirates_Titans")],
        [InlineKeyboardButton("Channel 2", url="https://t.me/TitanXBackup")]
        [InlineKeyboardButton("Channel 3", url="https://t.me/TitanXBots")]
    ]
    
    # Create the inline keyboard markup
    reply_markup = InlineKeyboardMarkup(buttons)
    
    # Send the introductory text with the inline keyboard
    message.reply_text(INTRO_TEXT, reply_markup=reply_markup)

# Start the bot
app.run()
