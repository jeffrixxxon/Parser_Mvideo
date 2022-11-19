import json
import logging
import time

from main_pagination import get_data
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
		get_data(data_category[message.text])
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
	with open('data/result_prices.json') as file:
		reader = json.load(file)
	cnt = 0
	for key, val in reader.items():

		# elif message.text is 'Restart 🔙':
		# 	await category(message.text)
		# 	break
		base_price = val.get('item_basePrice')
		sale_price = val.get('item_salePrice')
		card = f"Article number: {key}\n" \
		       f"Base price: {base_price} Руб.\n" \
		       f"Discounted price: {sale_price} Руб.\n" \
		       f"Discount: {int(abs((sale_price / base_price) * 100 - 100))}%"
		if int(num) <= abs((sale_price / base_price) * 100 - 100) <= int(num) + 10:
			time.sleep(2)
			await message.answer(card)
			cnt += 1
		elif message.text == 'View sale 😏':
			await parsing()
			break
	if cnt == 0:
		await message.answer('No items 😟')
	else:
		await message.answer(f'Number of products: {cnt}')


def main():
	executor.start_polling(dp)


if __name__ == '__main__':
	main()
