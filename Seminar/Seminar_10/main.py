from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *
from spy import *
import emoji


app = ApplicationBuilder().token("5691568503:AAFOTLoNs03dlDz--bSrXSmtoRxQYw_uAW0").build()



app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hi", hello_command))
app.add_handler(CommandHandler("echo", echo_command))
app.add_handler(CommandHandler("dt", time_command))
app.add_handler(CommandHandler("tem", tem_command))
app.add_handler(CommandHandler("call", call_command))


print(f'Server start ' + emoji.emojize(':check_mark_button:'))
app.run_polling()