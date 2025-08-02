import telebot

BOT_TOKEN = "8384058819:AAFVwPsIgToc9IW0Wv655fsCO6rdsZChyuE"

bot = telebot.TeleBot(BOT_TOKEN)

sticker_links = {
    "AgAD5RcAAs5ucFQ": "https://t.me/btodarkside/267"
}

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    file_id = message.sticker.file_unique_id
    print("Sticker ID:", file_id)
    if file_id in sticker_links:
        bot.send_message(message.chat.id, f"🔗 Here is your post:\n{sticker_links[file_id]}")
    else:
        bot.send_message(message.chat.id, "😕 I don't recognize this sticker.")

@bot.message_handler(func=lambda message: True)
def handle_other(message):
    bot.send_message(message.chat.id, "❗ Please use a sticker to get the post link.")

print("🤖 Bot is running...")
bot.polling()
