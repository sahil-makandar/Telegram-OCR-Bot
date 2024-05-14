#importing everything
from telegram.ext import *
from io import BytesIO
import cv2
import easyocr
import numpy as np

#Telegram bot access token from Bot father
TOKEN = "<telegram-bot-token>"

def start(update, context):
    #Conversation starting message
    update.message.reply_text("Welcome! Type something or send a picture")
    
def help(update, context):
        update.message.reply_text("""
                                  
         /start - starts conversation
         /help - shows this message                      
        
        """)
        
#text message handler
def handle_message(update, context):
    
    #responds with the same text 
    message = str("'"+update.message.text+"'")
    
    #send response
    update.message.reply_text(message)
    
    
#image input handler    
def handle_photo(update, context):

        #get the image from telegram bot
        file  = context.bot.get_file(update.message.photo[-1].file_id)
        
        #"""""""""PRE-PROCESSING"""""""""""#
        #convert the image to a bytearray
        f = BytesIO(file.download_as_bytearray())
        
        #Read the bytearray and store it in file_bytes for further use
        file_bytes = np.asarray(bytearray(f.read()), dtype=np.uint8)
        
        #decode the bytearray
        img = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        
        #adjusting the colours in image for preprocessing
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
   
        #"""""""""READING TEXT FROM IMAGE"""""""""""""#
        reader = easyocr.Reader(['en'], gpu=False)
        result = reader.readtext(img, detail=0,paragraph=True)
        
        print(result)
        
        #Removes the extra brackets from the start and end of string
        r = str(result).lstrip('[').rstrip(']')
        print(r)
        
        #Check if the string is empty (or the image does not have any text)
        if(r == ""):
            r=" Something went wrong... Please make sure the image has text...."        

        #send response 
        update.message.reply_text(r)
                        

#Initializing the telegram updater
updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

#Handlers for disfferent inputs
dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help))
dp.add_handler(MessageHandler(Filters.text, handle_message))
dp.add_handler(MessageHandler(Filters.photo, handle_photo))

updater.start_polling()
updater.idle()


