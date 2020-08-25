import pyarduino
import functions
import user_password

###############
from telegram.ext import Updater, MessageHandler, Filters
###############
needPassword = False
###############
def messageFilter(update, context):#This can filter messages
    global needPassword
    banned = functions.isBanned(update.message.from_user.id)
    if banned:
        answ="You are banned"
        update.message.reply_text(answ)
    else:
        logged = functions.isLoged(update.message.from_user.id)
        if logged:
            answ = functions.filterCommand(update.message.text, update.message.from_user.id)
        else:
            if needPassword == True:
                password = functions.login(update.message.text)
                if password:
                    functions.newUser(update.message.from_user.id, update.message.from_user.username)
                    answ = "Login complete"
                else:
                    answ = "Login failed, restart login"
                needPassword = False
            else:
                needWritePassword = functions.filterLogin(update.message.text)
                if needWritePassword:
                    answ = "Write the password"
                    needPassword = True
                else:
                    answ = "Error to login"
        update.message.reply_text(answ)

tk = user_password.token()
updater = Updater(token=tk, use_context=True)  #change the token

dp = updater.dispatcher

dp.add_handler(MessageHandler(Filters.text, messageFilter))

updater.start_polling()
updater.idle()