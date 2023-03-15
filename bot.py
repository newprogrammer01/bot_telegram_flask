from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
import os
from flask import Flask, request


TOKEN = os.environ['TOKEN']
app=Flask(__name__)
@app.route('/')
def start(update: Update, context:CallbackContext):
    chat_id=update.message.chat.id

    keyboar=ReplyKeyboardMarkup([
        ['Uzbek tili 🇺🇿', 'русский язык 🇷🇺']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, text='Iltimos tilni tanlang // Пожалуйста, выберите язык', reply_markup=keyboar)

def uzbek_tili(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=ReplyKeyboardMarkup([
        ["Ma'lumot olish ℹ️"],["Biz bilan bog'lanish 🌐"],['Orqaga qaytish ⬅️']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text="Assalomu alaykum hurmatli mijoz siz bu bot orqali bizning mahsulotlarimiz haqida malumot olishingiz hamda biz bilan bog'lanishingiz mumkin.")

def rus_tili(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=ReplyKeyboardMarkup([
        ['Получить информацию ℹ️'], ['связаться с нами 🌐'], ['возвращаться ⬅️']
    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text="Здравствуйте, уважаемый клиент, вы можете получить информацию о наших продуктах и ​​связаться с нами через этого бота.")
def boglanish_uzbekcha(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Telifon raqamimiz 📞", callback_data='tel_nomer_uz')],
        [InlineKeyboardButton(text="Bizning manzilimiz 🅰️", callback_data="manzil_uz")],
        [InlineKeyboardButton(text="Telegram kanalimiz 👥", url='https://t.me/sooft_uz')],
        [InlineKeyboardButton(text="Locatsiyamiz 📍", url='https://maps.app.goo.gl/qRtfHp1vHksMXUkx9')],
        [InlineKeyboardButton(text="Instagram profilimiz ", url="https://instagram.com/sooft_uz?igshid=YmMyMTA2M2Y=")]




    ])  
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar,text="Marxamat!")
def boglanish_ruscha(update:Update, context:CallbackContext):
    chat_id=update.message.chat.id
    keyboar=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="Наш номер телефона 📞", callback_data="tel_nomer_rus")],
        [InlineKeyboardButton(text="Наш адрес 🅰️", callback_data="manzil_rus")],
        [InlineKeyboardButton(text="Наш Telegram-канал 👥", url='https://t.me/sooft_uz')],
        [InlineKeyboardButton(text="Наше местоположение 📍", url='https://maps.app.goo.gl/qRtfHp1vHksMXUkx9')],
        [InlineKeyboardButton(text="Наш профиль в инстаграмм", url="https://instagram.com/sooft_uz?igshid=YmMyMTA2M2Y=")]

    ])
    bot=context.bot
    bot.sendMessage(chat_id=chat_id, reply_markup=keyboar, text="Пожалуйста, выбери!!!")
def query(update:Update, context:CallbackContext):
    query=update.callback_query
    chat_id=query.message.chat.id
    data=query.data
    bot=context.bot

    if data == 'tel_nomer_uz':
        bot.sendContact(chat_id=chat_id, phone_number=+998904776646,first_name="SOOFT_ADMIN")
    elif data=='manzil_uz':
        bot.sendMessage(chat_id=chat_id, text="📍Bizning manzilimiz Samarqand viloyati Jomboy tumani Farhod shaharchasi Shirin mahallasida joylashgan.\n😎 Yana bir gap, bizga masofa hech qanday to'sqinlik qila olmaydi. Chunki Sooftda tezkor va ehtiyotlab yetkazib berish xizmati ham mavjud")
    elif data=='tel_nomer_rus':
        bot.sendContact(chat_id=chat_id, phone_number=+998904776646, first_name="SOOFT_ADMIN")
    elif data=='manzil_rus':
        bot.sendMessage(chat_id=chat_id, text="📍Наш адрес находится в микрорайоне Ширин, г. Фарход, Жомбойский район, Самаркандская область.\n😎Потому что у Sooft также есть быстрая и точная служба доставки.")
    query.answer("Ok")



updater=Updater(token=TOKEN)
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Uzbek tili 🇺🇿'),uzbek_tili))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Orqaga qaytish ⬅️'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('русский язык 🇷🇺'), rus_tili))
updater.dispatcher.add_handler(MessageHandler(Filters.text('возвращаться ⬅️'), start))
updater.dispatcher.add_handler(MessageHandler(Filters.text("Biz bilan bog'lanish 🌐"),boglanish_uzbekcha))
updater.dispatcher.add_handler(MessageHandler(Filters.text('связаться с нами 🌐'),boglanish_ruscha))
updater.dispatcher.add_handler(CallbackQueryHandler(query))
updater.start_polling()
updater.idle()


if __name__ =='__main__':
    app.run()

