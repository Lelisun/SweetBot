# юда все функции отправляющие сообщения


from aiogram import types
from aiogram.dispatcher.filters.state import State
from bot import bot
import model, time


async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки.\n'
                           f'Всего есть 150 конфет, выиграет тот кто заберет все конфеты!\n'
                           f'Знай! Взять можно не более 28 конфеток!')

async def goodbye(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, это еще не конец! Начнем с начала!\n'
                           f'Будем играть до победы! Бери!')

async def botTurn(message: types.Message):
    if model.bot_qty == 0:
        await bot.send_message(message.from_user.id,f'Возьму пожалуй в другой раз!')
    else: await bot.send_message(message.from_user.id,f'Я взял {model.bot_qty} конфет!')
    
async def checkUserInput(message: types.Message, errType):
    match errType:
        case 0:
            await bot.send_message(message.from_user.id, 'А ты азартен Парамошка, не более 28 конфеток!')
        case 1:
           await bot.send_message(message.from_user.id, 'Попробуй еще раз, а лучше введи число!')

async def orderText(message: types.Message):
    if model.order == 1:
        await bot.send_message(message.from_user.id, 'Первый хожу я!')
    else: await bot.send_message(message.from_user.id, 'Первый ходишь ты!\nВведи количество конфет!')

async def sweetyCountText(message: types.Message):
    await bot.send_message(message.from_user.id,f'Осталось {model.total_count} конфет...')

async def inputSweetiesCount(message: types.Message):
    await bot.send_message(message.from_user.id,f'Введи количество конфет!')

async def noMoreSweeties(message: types.Message):
    await bot.send_message(message.from_user.id,f'Не осталось больше конфет(((')

async def isWinner(message: types.Message, whoWin):
    match whoWin:
        case "USER":
            await bot.send_message(message.from_user.id, f"Победа!")
            await goodbye(message)  
            model.total_count = 150
            
            
        case "BOT":
            await bot.send_message(message.from_user.id, f"Не сегодня, ты проиграл!")
            await goodbye(message)
            model.total_count = 150 
            

