from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commander import *
import emoji


app = ApplicationBuilder().token("Token").build()


app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("call", calculator_command))

print(f'Сервер запущен ' + emoji.emojize(':dizzy:'))

app.run_polling()