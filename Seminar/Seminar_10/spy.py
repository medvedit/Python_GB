from telegram import Update
from telegram.ext import CallbackContext
import datetime


def log(update: Update, context: CallbackContext):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}, {datetime.datetime.today()}\n')
    file.close()