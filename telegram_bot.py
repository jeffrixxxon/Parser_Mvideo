import json
import logging
import time

from main_pagination import get_data, get_result
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from auth_data import token, category_dict, category_list, generate_numbers

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


@dp.message_handler(Text(equals=['Go parsing! 👾', 'Restart 🔙']))
async def category(message: types.Message):
	start_buttons = category_list
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer('Choose a category 🗿', reply_markup=keyboard, )


@dp.message_handler(Text(equals=['View sale 😏']))
@dp.message_handler(Text(equals=category_list))
async def parsing(message: types.Message):
	data_category = category_dict
	start_buttons = generate_numbers
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)

	if message.text != 'View sale 😏':
		await message.answer('Please waiting... parsing procedure...')
		print(f'[INFO] {message.from_user.first_name} connected!')
		print(message)
		# get_data(data_category[message.text])
		# get_result()
		print('[!]Parsing complete')
		await message.answer('Complete ✅')
		time.sleep(1)
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )
	else:
		await message.answer('Complete ✅')
		time.sleep(1)
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )


@dp.message_handler(Text(equals=generate_numbers))
async def event_handler(message: types.Message):
	start_buttons = ['View sale 😏', 'Restart 🔙']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Complete ✅', reply_markup=keyboard)
	await search_sale(message)


@dp.message_handler(Text(equals=['Restart 🔙']))
async def search_sale(message: types.Message, num):
	with open('data/result.json.json') as file:
		reader = json.load(file)
	cnt = 0
	for elem in reader.items():
		data = elem.get('body').get('product')
		card = f"Product id: {data.get('productId')}\n" \
		       f"Name product: {data.get('name')}\n" \
		       f"Item base price: {data.get('item_basePrice')}\n" \
		       f"Item sale price: {data.get('item_salePrice')}\n" \
		       f"Item bonus: {data.get('item_bonus')}\n" \
		       f"Item sale: {data.get('item_sale')}\n" \
		       f"Item link: {data.get('item_link')}"

		if int(message.text) <= data.get('item_sale') < int(message.text) + 10:
			await message.answer(card)
	if cnt == 0:
		await message.answer('No items 😟')
	else:
		await message.answer(f'Number of products: {cnt}')


def main():
	executor.start_polling(dp)


if __name__ == '__main__':
	main()
