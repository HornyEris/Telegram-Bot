import telebot

BOT_TOKEN = "8384058819:AAFVwPsIgToc9IW0Wv655fsCO6rdsZChyuE"

bot = telebot.TeleBot(BOT_TOKEN)

sticker_responses = {
    "AgAD5RcAAs5ucFQ": "https://t.me/btodarkside/267"
}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Beyond The Oblivion Translation Team မှကြိုဆိုပါတယ်!\n\nကျေးဇူးပြုပြီး Sticker Set ကိုအရင်အသုံးပြုပေးပါ။\n👉 https://t.me/addstickers/BTO_Darkside")

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    sticker_id = message.sticker.file_id
    if sticker_id in sticker_responses:
        bot.send_message(message.chat.id, sticker_responses[sticker_id])
    else:
        bot.send_message(message.chat.id, "😕 ဒီStickerကိုမသိပါ။")

@bot.message_handler(func=lambda m: True)
def all_else(message):
    bot.send_message(message.chat.id, "⚠️ ကျေးဇူးပြုပြီး Sticker ကိုသုံးပြီး Post Link ကိုရယူပါ။")
