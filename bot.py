from telegram.ext import *
from io import BytesIO
import cv2
import numpy as np
import requests
import easyocr

TOKEN = "<telegram-bot-token>"

def start(update, context):
    update.message.reply_text("Welcome! Type something or send a picture")

def help(update, context):
    update.message.reply_text("""
         /start - starts conversation
         /help - shows this message
    """)

def handle_message(update, context):
    message = str("'"+update.message.text+"'")
    req = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})
    for i in req.json():
        update.message.reply_text(f"{i['text']}")

def handle_photo(update, context):
    try:
        file  = context.bot.get_file(update.message.photo[-1].file_id)
        f = BytesIO(file.download_as_bytearray())
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(img, detail=0, paragraph=True)
        r = str(result).lstrip('[').rstrip(']')
        if(r == ""):
            r=" Something went wrong... Please make sure the image has text...."
        req = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": r})
        for i in req.json():
            update.message.reply_text(f"{i['text']}")
    except Exception as e:
        print(str(e))

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))
dp.add_handler(MessageHandler(Filters.document.jpg, handle_photo))

updater.start_polling()
updater.idle()
