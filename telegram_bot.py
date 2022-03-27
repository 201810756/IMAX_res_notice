import telegram

bot=telegram.Bot(token='5266266718:AAGFHq4ytu1u_hBxFPiKKGD0a1ZHkRd0OC8')

"""for i in bot.getUpdates():
    print(i.message)"""
bot.sendMessage(chat_id=5179415817,text="테스트입니다")