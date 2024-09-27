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
            text = f"<b>✯ Creator : <a href='tg://user?id={OWNER_ID}'>This Person</a>\n✯ Language : <code>Python3</code>\n✯ Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n✯ Source Code : <a href='https://github.com/TitanXBots/FileStore-Bot'>Click here</a>\n✯ Channel : @TitanXBots\n✯ Support Group : @TitanMattersSupport</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/TitanXBackup/33')
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
