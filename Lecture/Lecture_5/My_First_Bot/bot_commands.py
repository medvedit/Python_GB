from telegram import Update
from telegram.ext import CallbackContext
import datetime
from spy import *

async def start_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n/data_time - Вывод дата и время\n'
                                    '/sum - Введите две цифры и я их сложу\nПример ввода: /sum 2 3 \n'
                                    '/help - Вывод всех команд')
async def hi_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'/hi - Приветствие\n/data_time - Вывод дата и время\n'
                                    '/sum - Введите две цифры и я их сложу\nПример ввода: /sum 2 3 \n'
                                    '/help - Вывод всех команд')

async def time_command(update: Update, context: CallbackContext):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.today().strftime("%A")}  '
                                    f'{datetime.datetime.today().strftime("%d.%m.%Y")}\n'
                                    f'{datetime.datetime.today().strftime("%H:%M:%S")}')

async def sum_command(update: Update, context: CallbackContext):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')