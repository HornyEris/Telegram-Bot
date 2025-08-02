import telebot

BOT_TOKEN = "8384058819:AAGTXt-cWULO5MDZEfCyuVksm3txrTkThDA"
bot = telebot.TeleBot(BOT_TOKEN)

sticker_links = {
    "AgAD5RcAAs5ucFQ": "https://t.me/btodarkside/267"
}

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    file_unique_id = message.sticker.file_unique_id
    print("Sticker ID:", file_unique_id)
    
    if file_unique_id in sticker_links:
        bot.send_message(
            message.chat.id,
            f"🔗 သင်ကြည့်ရှုလိုသော Hentai Link ရပါပြီ:\n{sticker_links[file_unique_id]}"
        )
    else:
        bot.send_message(message.chat.id, "😕 ဒီStickerကိုမသိပါ။")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,
        "👋 Beyond The Oblivion Translation Team မှကြိုဆိုပါတယ်!\n\n"
        "📌 ကျေးဇူးပြုပြီး Sticker Set ကိုအရင်အသုံးပြုပေးပါ။\n"
        "👉 https://t.me/addstickers/BTO_Darkside"
    )

@bot.message_handler(func=lambda message: True)
def handle_other(message):
    bot.send_message(message.chat.id, "⚠️ ကျေးဇူးပြုပြီး Sticker ကိုသုံးပြီး Post Link ကိုရယူပါ။")

print("🤖 Bot is running...")
bot.infinity_polling()
