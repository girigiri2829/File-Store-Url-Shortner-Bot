import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6465575067:AAFK1-BgRcPzfn_dCqi9RVSSin_QJ5iPMCI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23049826"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4a4216f089ce68a3ce2c8b9b9a6fa79a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001920761598"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2135601715"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://aman:hdhub4net@cluster0.f6fbxm4.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "hdhub4net")

#SHORTLINK
SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "api.shareus.io")
SHORTLINK_API = os.environ.get('SHORTLINK_API', "X5rPdPMFArX1bpMMZcsTJ5Qr9p53")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001559855851"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}✨\n\nWelcome To Gi All Serials Bot\nYou Can Watch TV Serials Of This Bot And You Will Old Serials On This Bot!")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1964685925 1781188088").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hi {mention} 💖\n\nWelcome To My Bot\nYou Can Watch Your Favorite Serial! Just Click "Join Channel" Button And Please Join My Channel And\nSend /start command And Watch Your Favorite Serial")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "<b>Hello {Full}\n\nAny Questions Or Any Serial Request 
@Gi_Serials_Owner_bot Connect Me Via This Bot! 👆</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(2135601715)

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
