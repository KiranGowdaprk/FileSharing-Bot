#TitanXBots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚓ ʜᴏᴍᴇ", callback_data = "start"),
                    InlineKeyboardButton("⚡ ᴄʟᴏꜱᴇ", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("🧠 ʜᴇʟᴘ", callback_data = "help"),
                    InlineKeyboardButton("🔰 ᴀʙᴏᴜᴛ", callback_data = "about")
                    ]
                ]
            )
        )            
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
