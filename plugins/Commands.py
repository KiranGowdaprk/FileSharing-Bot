import pyrogram
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import messages  # Example: import your message strings
from pyrogram import enums
from Script import script
from bot import Bot

# ... (Your existing bot logic) ...

@app.on_message(filters.command("start") & filters.private)
async def handle_start(client, message):
    # ... (Your start logic) ...
    
    # Send initial help message with buttons
    await message.reply_text(
        "Welcome! Choose an option:n",
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Help 🆘", callback_data="help")],
                [InlineKeyboardButton("About 🔰", callback_data="about")],
            ]
        ),
    )

@app.on_callback_query()
async def handle_callback(client, query):
    if query.data == "help":
        buttons = [
            [
                InlineKeyboardButton(
                    "• ʙᴏᴛ ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅꜱ •", callback_data="admin_commands"
                )
            ],
            [
                InlineKeyboardButton("• ᴜꜱᴇʀ •", callback_data="user_commands"),
            ],
            [
                InlineKeyboardButton("⇋ ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ ⇋", callback_data="start"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=messages.HELP_TXT.format(query.from_user.mention),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
        )
  

         # Information
  
    elif query.data == "about":
        buttons = [
            [
                InlineKeyboardButton(
                    "‼️ ᴅɪꜱᴄʟᴀɪᴍᴇʀ ‼️", callback_data="disclaimer"
                ),
            ],
            [
                InlineKeyboardButton("Sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data="Source"),
            ],
            [
                InlineKeyboardButton("My Developers 😎", callback_data="mydevelopers"),
            ],
            [
                InlineKeyboardButton("⇋ ʙᴀᴄᴋ ᴛᴏ ʜᴏᴍᴇ ⇋", callback_data="start"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=messages.ABOUT_TXT.format(temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
        )

 elif query.data == "mydevelopers":
        await query.answer(
            "Meet the minds behind this bot:nn👨‍💻 @Pirates_Titansn👨‍💻 @TitanOwnern👨‍💻 @TitanXBotsn👨‍💻 nn❤️ A big thank you for making this bot awesome!"
        )

    elif query.data == "Source":
        buttons = [
            [
                InlineKeyboardButton("Private Repo", url="https://t.me/TitanContactBot")
            ],
            [
                InlineKeyboardButton("• 𝗕𝗮𝗰𝗸 •", callback_data="about"),
                InlineKeyboardButton("• 𝗖𝗹𝗼𝘀𝗲 •", callback_data="close_data"),
            ],
        ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.message.edit_text(
            text=messages.SOURCE_TXT,
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML,
        )
      
