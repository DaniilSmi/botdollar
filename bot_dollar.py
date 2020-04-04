from telebot import types
import telebot
import requests
from bs4 import BeautifulSoup
import math


bot = telebot.TeleBot("1188312083:AAHT5keiLZ1hds2inPH9HGYDEB-bP17PQJ0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, 'Я говорю курс доллара, напиши "курс" и узнаешь его, или просто введи доллары и получишь их в рублях)))')

@bot.message_handler(content_types = ['text'])
def send_weather(message):
	loww = message.text.lower()
	if loww == "курс":
		news = 'https://www.google.com/search?sxsrf=ALeKk02cgu0bWJaNtzepRo_bYjjB70Bi9A%3A1585936541899&ei=nXiHXv_SNseLmwW83bOQCw&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQDDIECCMQJzIECAAQQzIECAAQQzIECAAQQzICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQsAIQJzoECAAQDToECAAQAVDmBliDXmDkaWgIcAB4AIABhAeIAYcYkgELMi0yLjMuMC4xLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi_ld2B6szoAhXHxaYKHbzuDLIQ4dUDCAs'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'}

		full = requests.get(news, headers=headers)

		soup = BeautifulSoup(full.content, 'html.parser')

		convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

		u = (convert[0].text)
		u = u.replace(',', '.')
		dollar = float(u)

		answer = 'Курс доллара сейчас = ' + str(dollar)+ 'руб' + '\n'

		if dollar < 77:
			answer += 'Пока ещё можно жить'
		else:
			answer += 'Всё плохо(('

	else:
		try:
			real = message.text
			real = real.replace(',', '.')
			real = float(real)
			news = 'https://www.google.com/search?sxsrf=ALeKk02cgu0bWJaNtzepRo_bYjjB70Bi9A%3A1585936541899&ei=nXiHXv_SNseLmwW83bOQCw&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQDDIECCMQJzIECAAQQzIECAAQQzIECAAQQzICCAAyAggAMgIIADICCAAyAggAMgIIADoHCCMQsAIQJzoECAAQDToECAAQAVDmBliDXmDkaWgIcAB4AIABhAeIAYcYkgELMi0yLjMuMC4xLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi_ld2B6szoAhXHxaYKHbzuDLIQ4dUDCAs'
			headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4100.3 Safari/537.36'}

			full = requests.get(news, headers=headers)

			soup = BeautifulSoup(full.content, 'html.parser')
			
			convert = soup.findAll("span", {"class": "DFlfde", "class": "SwHCTb", "data-precision": 2})

			u = (convert[0].text)
			u = u.replace(',', '.')

			dollar = float(u)
			dollar = dollar * real
			dollar = round(dollar)
			answer = str(real) + '$ = ' + str(dollar) + 'руб' + '\n'

			
		except ValueError:
			answer = 'Введите число, а не слово))'

	bot.send_message(message.chat.id, answer)





bot.polling( none_stop = True )