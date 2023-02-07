from telegram import Update
from telegram.ext import ContextTypes
from spy import *
from translator_deyweek import *
from function_calculator import *
from new_year_function import *
from text_function import *
from moon_function import *
from game_function import *
from time import sleep
import datetime
import emoji
import weather
import requests
from weather_update.weather import get_weather




async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Здравствуй {update.effective_user.first_name} ' + emoji.emojize('🤓\n') +
                                    'Вы видите весь список возможных команд: \n/hi -> Я здороваюсь ' + emoji.emojize('🤝\n') +
                                    '/dt -> Покажу день недели, дату и время ' + emoji.emojize('📅\n') +
                                    '/tem -> Покажу температуру воздуха в г.Киров ' + emoji.emojize('🌡️\n')+
                                    '/moon -> Расскажу о фазах луны ' + emoji.emojize('🌖\n') +
                                    '/new -> Посчитаю время до нового года' + emoji.emojize('🌲\n')+
                                    '/echo -> Буду повторять все Ваши фразы ' + emoji.emojize('📣\n') +
                                    '/call -> Я калькулятор' + emoji.emojize('🧮\n') +
                                    '/ph -> Мудрость дня' + emoji.emojize('📑\n')+
                                    '/game -> Игра ' + emoji.emojize('❌ ') + emoji.emojize('⭕\n') +
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
    '''Закомментированый ниже код не верно показывает температуру. Позже его изучу.'''
    try:
        weather = get_weather("Kirov,RU")
        await update.message.reply_text(f"Температура воздуха\nв городе Киров: {weather['main']['temp']}°C " + emoji.emojize('🌡️\n'))
    except:
        await update.message.reply_text(f'Сервер не всегда работает корректно. Попробуйте повторить ввод позже.')



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Вывод доступных команд + логирование'''
    log(update, context)
    await update.message.reply_text(f'/hi -> Здороваюсь.\n'+
                                    '/dt -> День недели, дата, время.\n'+
                                    '/tem -> Температура воздуха в г.Киров\n'+
                                    '/moon -> Фазы луны.\n'
                                    '/new -> Количество дней до нового года\n'+
                                    '/echo -> Повторю Вашу фразу.\n'+
                                    '/call -> Калькулятор.\n'+
                                    '/game -> Игра "Х/О".\n'+
                                    '/ph -> Мудрость дня')




async def new_year_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(new_year())



async def open_text_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(open_text())


async def moon_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Сегодня {moon_day()} лунный день.\n'+
                                    f'{moon_age()}\n{percent_moon()}\n{moon_phase()}')



async def message_processing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработка сырого текста в чате"""
    if update.message.text[0] != '/':
        if game.game_status:
            ''' запущена игра
                ход игрока'''
            try:
                matches = int(update.message.text)
            except:
                await update.message.reply_text('Я не понял ваш ответ. Напишите цифрой, какую позицию вы выбираете.')
                return
            if not 0 < matches < 10:
                await update.message.reply_text('Вы вышли за границы игрового поля')
                return
            game.action_player(matches)
            if game.check_game_state():
                await update.message.reply_text(f'Урааааааа!\n\n{game.showMatrix()} \nПоздравляю вас!\nВы выиграли!!!')
                game.stop()
                return
            if game.check_drawn_game():
                await update.message.reply_text(f'{game.showMatrix()} \nНичья')
                game.stop()
                return
            message = f'Ваш ход: \n{game.showMatrix()}'
            await update.message.reply_text(message)
            sleep(1)
            '''ход компьютера'''
            game.action_cpu()
            message = f'Ход компьютера: \n{game.showMatrix()}'
            await update.message.reply_text(message)
            sleep(1)
            if game.check_game_state():
                message = f'Я выиграл'
                await update.message.reply_text(message)
                game.stop()
                return
            if game.check_drawn_game():
                await update.message.reply_text(f'{game.showMatrix()} \nНичья')
                game.stop()
                return
            message = 'Ваш ход'
            await update.message.reply_text(message)
            return



async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    '''Игра Х & О'''
    log(update, context)
    if not game.game_status:
        game.start()
        message = f'Здравствуйте {update.effective_user.first_name}!\nВы готовы со мной сыграть в {game.help}' + emoji.emojize(' 🤓\n')
        sleep(1)
        await update.message.reply_text(message)
        message = f'* Игра началась *\n * Игровое поле *\n{game.showMatrix()}\n'
        sleep(2)
        await update.message.reply_text(message)
        if randint(1, 100) > 50:
            message = 'Я хожу первый\n'
            sleep(1)
            await update.message.reply_text(message)
            game.action_cpu()
            message = f'Ход компьютера: \n{game.showMatrix()}'
            await update.message.reply_text(message)
            sleep(1)
            await update.message.reply_text(f'Ваш ход')
        else:
            message = 'Ваш ход'
            await update.message.reply_text(message)

game = Game()