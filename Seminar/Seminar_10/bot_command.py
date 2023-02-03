from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *
from translator_deyweek import *
from function_calculator import *
from new_year_function import *
from text_function import *
import datetime
import emoji
import weather



async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуй {update.effective_user.first_name} ' + emoji.emojize('🤓\n') +
                                    'Вы видите весь список возможных команд: \n/hi -> Я здороваюсь ' + emoji.emojize('🤝\n') +
                                    '/echo -> Буду повторять все Ваши фразы ' + emoji.emojize('📣\n') +
                                    '/dt -> Покажу день недели, дату и время ' + emoji.emojize('📅\n') +
                                    '/tem -> Покажу температуру воздуха в г.Киров ' + emoji.emojize('🌡️\n')+
                                    '/call -> Я калькулятор' + emoji.emojize('🧮\n') +
                                    '/new -> Посчитаю время до нового года' + emoji.emojize('🌲\n')+
                                    '/text -> Мудрость дня' + emoji.emojize('📑\n')+
                                    '/help -> Окажу посильную мне помощь ' + emoji.emojize('⁉️'))




async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Здороваюсь + логирование'''
    log(update, context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name} ' + emoji.emojize(':handshake:'))




async def echo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Эхо ответ + логирование'''
    log(update, context)
    if update.message.text.split(' ')[1:] == []:
        await update.message.reply_text(f'Не верно Вы {update.effective_user.first_name} вводите текст' + emoji.emojize('😉\n')+
                                        f'Нужно ввести команду сразу за ней текст.\n'
                                       f'Пример: /echo Привет, как дела?')
    else:
        in_text = update.message.text.split(' ')[1:]
        out_text = ' '.join(in_text)
        await update.message.reply_text(out_text)




async def call_command(update: Update, context: CallbackContext):
    '''Калькулятор'''
    log(update, context)
    # await update.message.reply_text(calc(update.message.text.split(' ')[1]))
    if update.message.text.split(' ')[1:] == []:
        await update.message.reply_text(f'{update.effective_user.first_name},\n'
                                        f'Нужно ввести команду сразу за ней то, что мне нужно посчитать.\n'
                                       f'Пример: /call (3+2)*2')
    else:
        result = calc(update.message.text.split(' ')[1])
        x = update.message.text.split(' ')[1:]
        text = ' '.join(x)
        await update.message.reply_text(f'{text} = {result}')





async def time_command(update: Update, context: CallbackContext):
    '''День недели, дата, время + логирование'''
    log(update, context)
    await update.message.reply_text(f'{change(dey_week)}  '
                                    f'{datetime.datetime.today().strftime("%d.%m.%Y")}\n'
                                    f'        {datetime.datetime.today().strftime("%H:%M:%S")}')




async def tem_command(update: Update, context: CallbackContext):
    '''Температура воздуха(город указан в коде) + логирование'''
    log(update, context)
    await update.message.reply_text(f'Температура воздуха\nв городе Киров:'
                    f'{weather.forecast("Kirov", unit=weather.CELSIUS).tomorrow[datetime.datetime.today().strftime("%H:%M")].temp}'+
                        emoji.emojize('🌡️'))




async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Вывод доступных команд + логирование'''
    log(update, context)
    await update.message.reply_text(f'/hi -> Здороваюсь.\n'+
                                    '/dt -> День недели, дата, время.\n'+
                                    '/echo -> Повторю Вашу фразу.\n'+
                                    '/call -> Калькулятор.\n'+
                                    '/tem -> Температура воздуха в г.Киров\n'+
                                    '/new -> Количество дней до нового года\n'+
                                    '/text -> Мудрость дня')




async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(new_year())



async def open_text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(open_text())