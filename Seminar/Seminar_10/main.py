from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler
from bot_command import *
from spy import *
import emoji


app = ApplicationBuilder().token("TOKEN").build()



app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("hi", hello_command))
app.add_handler(CommandHandler("echo", echo_command))
app.add_handler(CommandHandler("dt", time_command))
app.add_handler(CommandHandler("tem", tem_command))
app.add_handler(CommandHandler("call", call_command))
app.add_handler(CommandHandler("new", new_year_command))
app.add_handler(CommandHandler("ph", open_text_command))
app.add_handler(CommandHandler("moon", moon_command))
app.add_handler(CommandHandler("game", game_command))
app.add_handler(MessageHandler(None, message_processing))


print(f'Server start ' + emoji.emojize(':check_mark_button:'))
app.run_polling()