import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6255830358:AAHtNJTMkIDN9N1sfOcJZSRRJgv9K6g_VXQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23049826"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4a4216f089ce68a3ce2c8b9b9a6fa79a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002123960666")

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
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001674621206"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {mention} 💫 Welcome To Gi All Serials Bot. You Can Watch TV Serials Of This Bot. How Are You?")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1964685925_1781188088").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {mention}/n/nYou need to join in my Channel to use me,/n/nKindly Please join my Channel")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Any Questions or Any Serial Request, Connect this bot @Gi_Serials_Owner_bot"

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
