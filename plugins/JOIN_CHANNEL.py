import os
from pyrogram import Client, filters, enums
from pyrogram.types import *
from pyrogram.errors import *

# Channel IDs (replace with your actual channel IDs)
F_SUB1 = int(os.environ.get('F_SUB1', '-1002071945738'))
F_SUB2 = int(os.environ.get('F_SUB2', '-1001972961497'))
F_SUB3 = int(os.environ.get('F_SUB3', '-1002489835580'))

@Client.on_message(filters.command("joinchannels") & filters.private)
async def join_channels(client: Client, message: Message):
    user_id = message.from_user.id

    member_statuses = {}
    keyboard_buttons = []

    for channel_id in [F_SUB1, F_SUB2, F_SUB3]:
        try:
            member = await client.get_chat_member(channel_id, user_id)
            if member.status in [enums.ChatMemberStatus.MEMBER, 
                                enums.ChatMemberStatus.ADMINISTRATOR, 
                                enums.ChatMemberStatus.OWNER]:
                member_statuses[channel_id] = "✅"
        except UserNotParticipant:
            # Get the invite link for the channel
            invite_link = await client.export_chat_invite_link(channel_id)

            channel = await client.get_chat(channel_id)
            channel_title = channel.title

            keyboard_button = InlineKeyboardButton(
                text=f"{channel_title}",
                url=invite_link
            )
            keyboard_buttons.append(keyboard_button)
            member_statuses[channel_id] = "❌"

    response = "**Join Channels**\n\n"
    for channel_id in [F_SUB1, F_SUB2, F_SUB3]:
        channel_title = (await client.get_chat(channel_id)).title
        response += f"{channel_title} {member_statuses[channel_id]}\n"

    if keyboard_buttons:
        keyboard = InlineKeyboardMarkup(
            [[button] for button in keyboard_buttons]
        )
        await message.reply_text(response, reply_markup=keyboard)
    else:
        await message.reply_text(response)
