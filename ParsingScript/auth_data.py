import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')

sales_numbers = [str(i) for i in range(10, 100, 10)]

buttons_search = ['Smartphones', 'Tablets', 'Laptops', 'Televisions', 'Refrigerators', 'Washing machines', 'View sale']

data_base_category = {'Smartphones': '205', 'Tablets': '195', 'Laptops': '118', 'Televisions': '1',
                      'Refrigerators': '159', 'Washing machines': '89'}