import requests
import wikipedia
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from bs4 import BeautifulSoup as BS

BOT_TOKEN = '6521026154:AAFnoBLYvL8k-exdMOsDUo9WmEPxBpIHtBc'
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

wikipedia.set_lang("uz")

t = requests.get('https://sinoptik.ua/погода-ташкент')
f = requests.get('https://sinoptik.ua/погода-андижан')
s = requests.get('https://sinoptik.ua/погода-сырдарья')
n = requests.get('https://sinoptik.ua/погода-навои')

menu = InlineKeyboardMarkup(row_width=1)
menu.add(InlineKeyboardButton(text="Ob-havo",callback_data=f'havo'))

catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text="Toshkent",callback_data=f'01'),
 InlineKeyboardButton(text="Andijon",callback_data=f'02'),
 InlineKeyboardButton(text="Sirdaryo",callback_data=f'03'),
 InlineKeyboardButton(text="Navoiy",callback_data=f'04')
)

@dp.message_handler(commands='start')
async def sd_messeg(message:types.Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} \mening botimga xush kelibsiz!!!",reply_markup=menu)


@dp.message_handler(commands=['help'])
async def sd_messeg(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name} \nQanday yordam kerak!!!")

@dp.callback_query_handler(text='havo')
async def nimadir(callback :types.CallbackQuery):
    await callback.message.answer(f'Viloyatni tanlang 🔎',reply_markup=catalog_list)

@dp.message_handler()
async def echo_message(message: Message):
    try:
        respons = wikipedia.summary(message.text)
        await message.answer(respons)
    except:
        await message.answer("Bunday malumot yoq!!!")


@dp.callback_query_handler(text='01')
async def tashkent(callback : types.CallbackQuery):
    html_t = BS(t.content,'html.parser')
    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
    await callback.message.answer(f'bugungi havo harorati\nmin:{t_min} \nmax:{t_max}')
@dp.callback_query_handler(text='02')
async def tashkent(callback : types.CallbackQuery):
    html_t = BS(f.content,'html.parser')
    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
    await callback.message.answer(f'bugungi havo harorati\nmin:{t_min} \nmax:{t_max}')
@dp.callback_query_handler(text='03')
async def tashkent(callback : types.CallbackQuery):
    html_t = BS(s.content,'html.parser')
    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
    await callback.message.answer(f'bugungi havo harorati\nmin:{t_min} \nmax:{t_max}')
@dp.callback_query_handler(text='04')
async def tashkent(callback : types.CallbackQuery):
    html_t = BS(n.content,'html.parser')
    for el in html_t.select('#content'):
        min = el.select('.temperature .min')[0].text
        max = el.select('.temperature .max')[0].text
        t_min = min[4:]
        t_max = max[5:]
    await callback.message.answer(f'bugungi havo harorati\nmin:{t_min} \nmax:{t_max}')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)