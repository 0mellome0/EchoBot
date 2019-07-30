import telebot

bot = telebot.TeleBot("957042532:AAEUX4L7hp_D3NFql5YZXetvp4KWIHrWoU0")

@bot.message_handler(content_types=["text", "sticker", "photo", "audio"])
def send_welcome(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
