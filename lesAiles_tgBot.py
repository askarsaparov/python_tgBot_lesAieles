# python_tgBot_lesAiles
import telebot
from telebot import types

bot = telebot.TeleBot('1648917738:AAG4daDffNF37NxPnkPLqVH06d1H4JQ_Tks')
menus = ['💸Cashback', '🎉Tadbirlar', '✍️Fikr bildirish', "ℹ️Ma'lumot"]
def start_button():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    markup.row(telebot.types.KeyboardButton('🛍Buyrtma berish'))
    markup.add(*[
        telebot.types.KeyboardButton(text) for text in menus
    ])
    markup.row(
        telebot.types.KeyboardButton('⚙️Sozlamalar')
    )
    return markup

buyrtma = ['🚘Yetkazib berish', '🏃Olib ketish']
def buyrtma_berish():
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=1)
    markup.add(*[
        telebot.types.KeyboardButton(text) for text in buyrtma
    ])
    markup.row(
        telebot.types.KeyboardButton('⬅️Orqaga')
    )
    return markup

def location():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=1)
    markup.row(types.KeyboardButton(text='📍Eng yaqin shaxobchamizni aniqlash', request_location=True))
    markup.row(types.KeyboardButton('⬅️Orqaga'))
    return markup

loca = ['Joylashuvni qayta jo`natish📍', '☑️Tasdiqlash']
def joylashuv():
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=1)
    markup.add(*[
        types.KeyboardButton(text) for text in loca
    ])
    markup.row(
        telebot.types.KeyboardButton('⬅️Orqaga')
    )
    return markup
oxirgi = ['📥 Savat', '🚘 Buyurtma berish', '🍱Setlar', '🍔 Burgerlar', '🌯 Lesterlar', '🌭 Longer/Hot-dog', '🍗 Tovuqcha'\
          '🍟 Snekla', '🥗 Salatlar', '🎁 Bolalar uchun', '🍰 Десерты', '☕️ Ichimliklar', '😋 Souslar', '']
def savat():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=2)
    markup.add(*[
        types.KeyboardButton(text) for text in oxirgi
    ])
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.from_user.id,
        'Juda yaxshi! Birgalikda buyurtma beramizmi? 😁',
        reply_markup=start_button()
                    )

@bot.message_handler(func=lambda message: True)
def start_message(message):
    if message.text == '🛍Buyrtma berish':
        text = "Buyrtmani <b>o`zingiz</b> olib keting yoki <b>Yetkazib berishni</b> tanlang"
        bot.send_message(
            message.from_user.id,
            text,
            parse_mode='HTML',
            reply_markup=buyrtma_berish()
        )
    elif message.text == '🚘Yetkazib berish':
        text = "Buyurtmangizni qaerga yetkazib berish kerak 🚙?\
Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni va yetkazib berish xarajatlarini aniqlaymiz 💵"
        bot.send_message(
            message.from_user.id,
            text,
            reply_markup = location()
        )
    elif message.text == '☑️Tasdiqlash':
        text = '10:00 - 22:00 - 1 km gacha bo’lgan buyurtmalar yetkazish narxi 5000 so’m\
 10:00 - 22:00 - 3 km gacha 9000 so’m keyingi har 1 km uchun -1000 sum Toshkent shahri bo’ylab.'
        bot.send_message(
            message.from_user.id,
            text,
            reply_markup=savat()
        )
    


@bot.message_handler(content_types=['location'])
def location_m(message):
    text = "Sizning manzilingiz: Узбекистан, Ташкент, улица Козитарнов, 50\
    \
    Joylashuv natug'rimi?\
    Qayta jo'nating 📍"
    bot.send_message(message.from_user.id, text, reply_markup=joylashuv())


bot.polling(none_stop=True)
