from telegram.ext import ApplicationBuilder, CommandHandler
from bot_commands import *

app = ApplicationBuilder().token('5691568503:AAFOTLoNs03dlDz--bSrXSmtoRxQYw_uAW0').build()

app.add_handler(CommandHandler('start', start_command))
app.add_handler(CommandHandler('hi', hi_command))
app.add_handler(CommandHandler('data_time', time_command))
app.add_handler(CommandHandler('help', help_command))
app.add_handler(CommandHandler('sum', sum_command))


print('server start')

app.run_polling()