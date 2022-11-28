# Здесь храним все переменные и методы для их чтения и установки (а-ля работа с классами)

import random


total_count = 150
bot_qty = 0
order = 0
user_qty = 0

def botQtyChoose():
    global total_count
    global bot_qty
    if total_count > 0:
            if total_count < 29: fbot_qty = total_count
            elif total_count < 56: fbot_qty = 28
            else: fbot_qty = random.randint(0, 28)
            if fbot_qty != 0:
                total_count -= fbot_qty
            print(f"БОТ: {fbot_qty}")
            print(total_count)
            bot_qty = fbot_qty

def orderChoose():
    global order
    i = random.randint(0,1)
    order = i

def userQtyChoose():
    global total_count
    # import commands 
    # user_qty = commands.getNumber
    print(f"ЮЗЕР: {user_qty}")
    total_count = total_count - user_qty
    print(total_count)



