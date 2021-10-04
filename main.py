import telebot
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyKeyboardRemove,KeyboardButton, ForceReply
import moviepy.editor as m
import os

TOKEN = 'bot token'

bot = telebot.TeleBot(TOKEN, parse_mode="markdown")

@bot.message_handler(commands=['start'])
def start(msg):
    user_id = msg.chat.id
    bot.send_message(msg.chat.id, "👋 *Salom, menga birorta video yuboring\nMen sizga videodagi audioni yuboraman*[!](https://telegra.ph/file/27bc950c8e5cf94e24011.jpg)")

@bot.message_handler(content_types=['video'])
def convert(msg):
	bot.send_message(msg.chat.id,'⏳ _Kuting, bu biroz vaqt olishi mumkin!_')
	try:
		file_id = msg.video.file_id
		file = bot.get_file(file_id)
		file_path = file.file_path
		s = bot.download_file(file_path)
		with open(f'{msg.chat.id}.mp4', 'wb') as new_file:
			new_file.write(s)
		with m.VideoFileClip(f'{msg.chat.id}.mp4') as clip:
			clip.audio.write_audiofile(f"{msg.chat.id}.mp3")
		with open(f"{msg.chat.id}.mp3",'rb') as muzik:
			bot.send_audio(msg.chat.id,muzik)
		os.unlink(f'{msg.chat.id}.mp4')
		os.unlink(f'{msg.chat.id}.mp3')
	except Exception as ex:
		bot.send_message(msg.chat.id,'Xatolik!')
		print(f"{ex}")

bot.polling()
