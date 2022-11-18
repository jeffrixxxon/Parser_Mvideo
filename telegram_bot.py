import json
import logging
import time

from main_pagination import get_data
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from auth_data import token

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


@dp.message_handler(Text(equals=['Stop 🔚']))
async def stop(message: types.Message):
	await start(message)


@dp.message_handler(Text(equals=['Go parsing! 👾', 'Restart 🔙']))
async def category(message: types.Message):
	start_buttons = ['Smartphones 📱', 'Tablets 📲', 'Laptops 💻', 'Televisions 📺', 'Refrigerators 🚪', 'Washing machines 🧼']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)

	await message.answer('Choose a category 🗿', reply_markup=keyboard, )


@dp.message_handler(Text(equals=['View sale 😏']))
@dp.message_handler(Text(equals=['Smartphones 📱', 'Tablets 📲', 'Laptops 💻', 'Televisions 📺', 'Refrigerators 🚪', 'Washing machines 🧼']))
async def parsing(message: types.Message):
	data_category = {'Smartphones 📱': '205', 'Tablets 📲': '195', 'Laptops 💻': '118', 'Televisions 📺': '1', 'Refrigerators 🚪': '159', 'Washing machines 🧼': '89'}
	start_buttons = [str(i) for i in range(10, 100, 10)]
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Please waiting... parsing procedure...')
	if message.text != 'View sale 😏':
		get_data(data_category[message.text])
		print('[!]Parsing complete')
		print(f'[INFO] {message.from_user.first_name} parsit!')
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )
		await message.answer('Complete ✅')
	else:
		await message.answer('Enter the tracked discount 💲💲💲', reply_markup=keyboard, )
		await message.answer('Complete ✅')


@dp.message_handler(Text(equals=[str(i) for i in range(10, 100, 10)]))
async def search_sale(message: types.Message):
	start_buttons = ['Restart 🔙', 'Stop 🔚', 'View sale 😏']
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	keyboard.add(*start_buttons)
	await message.answer('Complete ✅', reply_markup=keyboard)
	with open('data/result_prices.json') as file:
		reader = json.load(file)
	cnt = 0
	for key, val in reader.items():
		base_price = val.get('item_basePrice')
		sale_price = val.get('item_salePrice')
		card = f"Article number: {key}\n" \
		       f"Base price: {base_price} Руб.\n" \
		       f"Discounted price: {sale_price} Руб.\n" \
		       f"Discount: {int(abs((sale_price / base_price) * 100 - 100))}%"
		if message.text == 'Stop 🔚':
			await stop(message)
		if abs((sale_price / base_price) * 100 - 100) >= int(message.text):
			time.sleep(2)
			await message.answer(card)
			cnt += 1
	if cnt == 0:
		await message.answer('No items 😟')
	elif message.text == 'View sale 😏':
		await parsing()
	elif message.text == 'Restart 🔙':
		await category(message.text)
	elif message.text == 'Stop 🔚':
		await stop(message.text)


def main():
	executor.start_polling(dp)


if __name__ == '__main__':
	main()
