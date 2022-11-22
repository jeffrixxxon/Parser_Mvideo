import json
import logging
import os
import time

from main_pagination import get_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from auth_data import token, sales_numbers

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start', )
async def start(message: types.Message):
	await message.answer(f'Hello, {message.from_user.first_name}! 👋🏻')
	start_buttons = ['Go parsing! 👾']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Choose a parsing mod 🤌🏻', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Go parsing! 👾', 'Back 🔙']))
async def category(message: types.Message):
	start_buttons = ['Smartphones 📱', 'Tablets 📲', 'Laptops 💻', 'Televisions 📺', 'Refrigerators 🚪', 'Washing machines 🧼', 'View sale 😏']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer('Choose a category 🗿', reply_markup=keyboard)


@dp.message_handler(Text(equals=['View sale 😏']))
@dp.message_handler(Text(equals=['Smartphones 📱', 'Tablets 📲', 'Laptops 💻', 'Televisions 📺', 'Refrigerators 🚪', 'Washing machines 🧼', 'View sale 😏']))
async def parsing(message: types.Message):
	data_category = {'Smartphones 📱': '205', 'Tablets 📲': '195', 'Laptops 💻': '118', 'Televisions 📺': '1',
	                 'Refrigerators 🚪': '159', 'Washing machines 🧼': '89'}
	start_buttons = [*sales_numbers, 'Back 🔙']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	if message.text != 'View sale 😏':
		await message.answer('Please waiting... parsing procedure...')
		print(f'[INFO] {message.from_user.first_name} connected!')
		try:
			os.remove(f'data/{message.from_user.first_name}_result.json')
		except FileNotFoundError:
			pass
		get_data(data_category[message.text], message.from_user.first_name)
		print('[!]Parsing complete')
		await message.answer('Complete ✅')
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )
	else:
		await message.answer('Complete ✅')
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )


@dp.message_handler(Text(equals=sales_numbers))
async def event_handler(message: types.Message):
	start_buttons = ['View sale 😏', 'Back 🔙']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Complete ✅', reply_markup=keyboard)
	await search_sale(message)


@dp.message_handler(Text(equals=['Back 🔙']))
async def search_sale(message: types.Message):
	with open(f'data/{message.from_user.first_name}_result.json') as file:
		reader = json.load(file)
	cnt = 0
	for key, val in reader.items():
		if int(message.text) <= val["item_sale"] < int(message.text) + 10:
			card = f'{hlink(val["item_name"], val["item_link"])}\n' \
			       f'Article: {key}\n' \
			       f'Base price: {val["item_basePrice"]} Руб.\n' \
			       f'Sale price: {val["item_salePrice"]} Руб.\n' \
			       f'Bonus: {val["item_bonus"]} ББ\n' \
			       f'Sale: {val["item_sale"]} %\n\n'
			await message.answer(card)
			cnt += 1
			time.sleep(1)
	if cnt == 0:
		await message.answer('No items 😟')
	else:
		await message.answer(f'Number of products: {cnt}')


def main():
	executor.start_polling(dp)


if __name__ == '__main__':
	main()
