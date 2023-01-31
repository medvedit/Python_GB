from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import emoji



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi => Тут я здороваюсь ' + emoji.emojize(':cowboy_hat_face:\n') +
                                    '/help => Вывод всех команд\n' + '/call => Калькулятор')

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Здравствуй {update.effective_user.first_name} ' + emoji.emojize(':thumbs_up:'))

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi => Тут я здороваюсь ' + emoji.emojize(':cowboy_hat_face:\n'))

async def calculator_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    x = update.message.text(update.chat.id, 'привет, введи любой текст и отправь')

    # x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))

    await update.message.reply_text(f'{x} + {y} = {x+y}')
