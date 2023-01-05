import json
import logging
import os
import time

from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hlink
from aiogram import Bot, Dispatcher, executor, types
from main_pagination import get_site_parsing_data
from auth_data import token, sales_numbers, buttons_search, data_base_category

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
	"""Greeting the user and selecting the operating mode"""

	await message.answer(f'Hello, {message.from_user.first_name}!')
	start_buttons = ['Go parsing!']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Choose a parsing mod', reply_markup=keyboard)


@dp.message_handler(Text(equals=['Go parsing!', 'Back']))
async def category(message: types.Message):
	"""Stub function for category selection"""

	start_buttons = buttons_search
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Choose a category', reply_markup=keyboard)


@dp.message_handler(Text(equals=['View sale']))
@dp.message_handler(Text(equals=buttons_search))
async def parsing(message: types.Message):
	"""Parse the entered category and returns the result of the 'get_data' function"""

	data_category = data_base_category
	start_buttons = [*sales_numbers, 'Back']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	if message.text != 'View sale':
		await message.answer('Please waiting... parsing procedure...')
		print(f'[INFO] {message.from_user.first_name} connected!')
		try:
			os.remove(f'data/{message.from_user.first_name}_result.json')
		except FileNotFoundError:
			pass

		get_site_parsing_data(data_category[message.text], message.from_user.first_name)
		print('[INFO]Parsing complete')

		await message.answer('Enter the tracked discount', reply_markup=keyboard, )
	else:
		await message.answer('Enter the tracked discount', reply_markup=keyboard)


@dp.message_handler(Text(equals=sales_numbers))
async def event_handler(message: types.Message):
	"""Function to return to 'category[Back]' or 'parsing[View sale]'"""

	start_buttons = ['View sale', 'Back']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Complete', reply_markup=keyboard)
	await search_sale(message)


async def search_sale(message: types.Message):
	"""Checking the result of the 'get_data' function for the selected discount"""

	with open(f'data/{message.from_user.first_name}_result.json') as file:
		reader = json.load(file)

	counter_items = 0

	for key, val in reader.items():
		if int(message.text) <= val["item_sale"] < int(message.text) + 10:
			card = f'{hlink(val["item_name"], val["item_link"])}\n' \
			       f'Article: {key}\n' \
			       f'Base price: {val["item_basePrice"]} Руб.\n' \
			       f'Sale price: {val["item_salePrice"]} Руб.\n' \
			       f'Bonus: {val["item_bonus"]} ББ\n' \
			       f'Sale: {val["item_sale"]} %\n\n'
			await message.answer(card)
			counter_items += 1
			time.sleep(1)
	if counter_items == 0:
		await message.answer('No items')
	else:
		await message.answer(f'Number of products: {counter_items}')


def main():
	executor.start_polling(dp)


if __name__ == '__main__':
	main()
