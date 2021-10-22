"""
            © Cyril C Thomas
            © https://t.me/c_text_bot
            © https://t.me/c_bots_support
"""

import os

class Config():
    #Get from @Botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    #Get from my.telegram.org
    API_ID = int(os.environ.get("API_ID", ))
    #Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "")
    #Time Required to sleep Before Posting New Message
    SLEEP_TIME = int(os.environ.get("SLEEP_TIME", ))
    #Channel ID, get from @RawDataBot
    CHAT_ID = int(os.environ.get("CHAT_ID", ))
    #Message Text
    MSG_TXT = os.environ.get("MSG_TXT", "")
    #Button Text
    BUTTON_TXT = os.environ.get("BUTTON_TXT", "")
    #Button URL
    BUTTON_URL = os.environ.get("BUTTON_URL", "")
