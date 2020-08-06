import pyarduino
import functions
##############
from telegram.ext import Updater, MessageHandler, Filters
##############
needPassword = False

def echo(update, context):
    global needPassword
    logged = functions.isLoged(update.message.from_user.id)
    if logged:
        rta = functions.filterCommand(update.message.text, update.message.from_user.id)
    else:
        if needPassword == True:
            password = functions.login(update.message.text)
            if password:
                rta = "Login complete"
                functions.newUser(update.message.from_user.id, update.message.from_user.username)
            else:
                rta = "Login failed, restart login"
            needPassword = False
        else:
            needWritePassword = functions.filterLogin(update.message.text)
            if needWritePassword:
                rta = "Write the password"
                needPassword = True
            else:
                rta = "Error to login"
    update.message.reply_text(rta)

tk = "YOUR TOKEN"
updater = Updater(token=tk, use_context=True)  #change the token

dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()