import os
import time
import telegram

from dotenv import load_dotenv


def pub_image():
    telegram_token = os.environ.get("TELEGRAM_TOKEN")
    delay = int(os.environ.get("PUBLISH_DELAY", 86400))
    telegram_channel = os.environ.get("TELEGRAM_CHANNEL")
    bot = telegram.Bot(token=telegram_token)
    while True:
        for dpath, dirnames, fnames in os.walk("images"):
            for fname in fnames:
                bot.send_document(
                    chat_id=telegram_channel,
                    document=open(file=os.path.join(dpath, fname), mode="rb")
                    )
        time.sleep(delay)


if __name__ == "__main__":
    load_dotenv()
    pub_image()
