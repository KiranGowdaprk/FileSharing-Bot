class script(object):
    START_TXT = """<b>ʜᴇʏ {}, {}\n\nɪ ᴀᴍ ʟᴀᴛᴇꜱᴛ ᴀɴᴅ ᴀᴅᴠᴀɴᴄᴇᴅ ᴘᴏᴡᴇʀꜰᴜʟ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴍᴇ ᴛᴏ ꜱᴛᴏʀᴇ ꜰɪʟᴇꜱ !! 😍\n<blockquote>🌿 ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href="https://t.me/TitanXBots">TitanXBᴏᴛs</a></blockquote></b>"""
    
    
    CAPTION = """<b>📂 ғɪʟᴇɴᴀᴍᴇ : {file_name}
    
Qury: For More Movies and Web Series [Click Here](https://t.me/Pirates_Titans)</b>""" 


    ABOUT_TXT = """<b>ʜɪ ɪ ᴀᴍ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ ᴡɪᴛʜ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ + ᴄᴜsᴛᴏᴍ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ɪᴛ ᴍᴇᴀɴs ᴀɴʏ ᴜsᴇʀ ᴄᴀɴ sᴇᴛ ʜɪs ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀɴᴅ + ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ.

🤖 ᴍʏ ɴᴀᴍᴇ: {}

📝 ʟᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>𝐏𝐲𝐭𝐡𝐨𝐧𝟑</a>

📚 ʟɪʙʀᴀʀʏ: <a href=https://docs.pyrogram.org>𝐏𝐲𝐫𝐨𝐠𝐫𝐚𝐦</a>

🧑🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href=https://t.me/TitanOwner>𝐘𝐚𝐬𝐡</a>

👥 sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/TitanMattersSupport>𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩</a>

📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/TitanXBots>𝐓𝐢𝐭𝐚𝐧𝐗𝐔𝐩𝐝𝐚𝐭𝐞𝐬</a></b>
"""
    
    
    HELP_TXT = """<b>💢 Hᴏᴡ Tᴏ Usᴇ Tʜɪs Bᴏᴛ ☺️

🔻 /link - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴠɪᴅᴇᴏ ᴏʀ ғɪʟᴇ ᴛᴏ ɢᴇᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ

🔻 /batch - sᴇɴᴅ ғɪʀsᴛ ʟɪɴᴋ ᴏғ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ ᴘᴏsᴛ ᴛʜᴇɴ ʟᴀsᴛ ᴘᴏsᴛ ʟɪɴᴋ ᴀɴᴅ ᴍᴀᴋᴇ sᴜʀᴇ ʙᴏᴛ ɪs ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ᴄʜᴀɴɴᴇʟ.
ᴇx - /batch https://t.me/what_if_season_2_hindi_dubb/13 https://t.me/what_if_season_2_hindi_dubb/14

🔻 /base_site - ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ sᴇᴛ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ʟɪɴᴋ ᴅᴏᴍᴀɪɴ 
ᴇx - /base_site ʏᴏᴜʀᴅᴏᴍᴀɪɴ.ᴄᴏᴍ

🔻 /api - sᴇᴛ ʏᴏᴜʀ ᴜʀʟ sʜᴏʀᴛɴᴇʀ ᴀᴄᴄᴏᴜɴᴛ ᴀᴘɪ 
ᴇx - /api ʙᴀᴏᴡɢᴡᴋʟᴀᴀʙᴀᴋʟ

🔻 /deletecloned - ᴜsᴇ ᴛʜɪs ғᴏʀ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ ʙᴏᴛ 
ᴇx - /deletecloned ʏᴏᴜʀʙᴏᴛᴛᴏᴋᴇɴ

🔻 /broadcast - ʀᴇᴘʟʏ ᴛᴏ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ʙʀᴏᴀᴅᴄᴀsᴛ (ʙᴏᴛ ᴏᴡɴᴇʀ ᴏɴʟʏ)</b>"""


     SOURCE_TXT = """<b>ɴᴏᴛᴇ:
- ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴀɴ ᴘʀɪᴠᴀᴛᴇ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.
- ꜱᴏᴜʀᴄᴇ - <a href="https://t.me/TitanXBots">ʜᴇʀᴇ</a>
Dᴇᴠᴇʟᴏᴘᴇʀ:
- <a href="https://t.me/TitanOwner">Yash</a></b>"""


    LOG_TEXT = """<b>#NewUser
    
ID - <code>{}</code>

Nᴀᴍᴇ - {}

By @TitanXBots</b>
"""

    
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !

📅 Dᴀᴛᴇ : <code>{}</code>
⏰ Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code>
🛠️ Bᴜɪʟᴅ Sᴛᴀᴛᴜs: <code>v2.7.1 [ Sᴛᴀʙʟᴇ ]</code>

By @TitanXBots</b>"""


    Logo = """
████████╗██╗████████╗░█████╗░███╗░░██╗██╗░░██╗██████╗░░█████╗░████████╗░██████╗
╚══██╔══╝██║╚══██╔══╝██╔══██╗████╗░██║╚██╗██╔╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
░░░██║░░░██║░░░██║░░░███████║██╔██╗██║░╚███╔╝░██████╦╝██║░░██║░░░██║░░░╚█████╗░
░░░██║░░░██║░░░██║░░░██╔══██║██║╚████║░██╔██╗░██╔══██╗██║░░██║░░░██║░░░░╚═══██╗
░░░██║░░░██║░░░██║░░░██║░░██║██║░╚███║██╔╝╚██╗██████╦╝╚█████╔╝░░░██║░░░██████╔╝
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═════╝░"""
