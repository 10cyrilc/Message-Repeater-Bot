"""
            © Cyril C Thomas
            © https://t.me/c_text_bot
            © https://t.me/c_bots_support
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from config import Config
import time

if Config.BUTTON_TXT  != "" and Config.BUTTON_URL != "":
    button_field = InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(Config.BUTTON_TXT, url=Config.BUTTON_URL)
                                 ]])
else:
    button_field = None

bot = Client("MSG BOT",
        bot_token=Config.BOT_TOKEN,
        api_id=Config.API_ID,
        api_hash=Config.API_HASH
        )
def main():
    with bot:
        while True:
            mes = bot.send_message(chat_id=Config.CHAT_ID,
                            text=Config.MSG_TXT,
                            reply_markup=button_field,
                            disable_web_page_preview=True,        
                            parse_mode="html")
            time.sleep(Config.SLEEP_TIME * 60)
            mes.delete()
if __name__ == "__main__":
    print("\n\nIf you have Any Issues Report it @c_text_bot\n\nor at https://t.me/c_text_bot\n\n")
    main()
else:
    print("Something is Wrong...... Contact @c_text_bot\n\nor https://t.me/c_text_bot")
