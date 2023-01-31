from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commander import *
import emoji

app = ApplicationBuilder().token("6089710413:AAEUiTHzXCYM-O03trnXs3g3nE4CEkFZnI0").build()


app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("cal", calculator_command))

print(f'Сервер запущен ' + emoji.emojize(':dizzy:'))

app.run_polling()