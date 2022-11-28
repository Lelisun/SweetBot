# Здесь что-то типа контроллера связывающий хендлеры и вью

from aiogram import types

import view

async def start(message: types.Message):
    import model
    model.orderChoose()
    await view.greetings(message)
    await view.orderText(message)
    if model.order == 1: 
        model.botQtyChoose()
        await view.botTurn(message)
        await view.sweetyCountText(message)

async def finish(message: types.Message):
    await view.goodbye(message)

async def getNumber(message: types.Message):
    import model
    number = message.text
    if number.isdigit():
        if 0 < int(number) < 29:
            model.user_qty = int(number)
            model.userQtyChoose()
            if model.total_count <= 0 :
                 await view.noMoreSweeties(message) 
                 await view.isWinner(message, "USER")  
                 return exit
                #  model.total_count = 150 
            await view.sweetyCountText(message) 
            model.botQtyChoose()
            await view.botTurn(message)
            if model.total_count <= 0:
                 await view.noMoreSweeties(message) 
                 await view.isWinner(message, "BOT") 
                 return exit
                #  model.total_count = 150
            await view.sweetyCountText(message)
            await view.inputSweetiesCount(message)
        else:
            await view.checkUserInput(message, 0)
    else: await view.checkUserInput(message, 1) 