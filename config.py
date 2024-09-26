#TitanXBots




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7446289564:AAH_V1d4D2wGDNc8Wx5I7sHBhNPm2hEMG1Y")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12293838"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cf8c7db0d609148786e7ca5c706909bd")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002096962621"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "YASH")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "5356695781"))
#Port
PORT = os.environ.get("PORT", "8080")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://TITANBOT1:TITANBOT1@cluster0.77yw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "TitanX")
#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002071945738"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001972961497"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://envs.sh/SP_.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://envs.sh/SPj.jpg")

HELP_TXT = "<b>ᴛʜɪs ɪs ᴀɴ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡᴏʀᴋ ғᴏʀ @Pirates_Titans\n\n✵ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/Pirates_Titans>ʏᴀꜱʜ</a></b>"
ABOUT_TXT = "<b>✯ᴍʏ ɴᴀᴍᴇ: ʏᴀꜱʜ\n✯ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/TitanContactBot>ʏᴀꜱʜ</a>\n✯ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Pirates_Titans>ᴛɪᴛᴀɴ ɴᴇᴛᴡᴏʀᴋ</a>\n✯ ʟɪʙʀᴀʀʏ : ᴘʏʀᴏɢʀᴀᴍ\n✯ ʟᴀɴɢᴜᴀɢᴇ: ᴘʏᴛʜᴏɴ\n✯ ᴅᴀᴛᴀʙᴀꜱᴇ: ᴍᴏɴɢᴏ ᴅʙ\n✯ ʜᴏꜱᴛᴇᴅ ᴏɴ: ᴀʟʟ ᴡᴇʙ</b>"
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello {first}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.</b>")
try:
    ADMINS=[5356695781]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• ʙʏ @Pirates_Titans</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "⭐ʜᴇʏ ʙʀᴏ ᴅᴏɴ'ᴛ ꜱᴇɴᴅ ᴍᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴅɪʀᴇᴄᴛʟʏ ɪ'ᴍ ᴏɴʟʏ ꜰɪʟᴇ ꜱʜᴀʀᴇ ʙᴏᴛ!"

ADMINS.append(OWNER_ID)
ADMINS.append(5356695781)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
