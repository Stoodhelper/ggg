from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

fruit=InlineKeyboardMarkup(row_width=4)
f1=InlineKeyboardButton(text='Бананы')
f2=InlineKeyboardButton(text='Сливы')
f3=InlineKeyboardButton(text='Виноград')
f4=InlineKeyboardButton(text='Персики')
f5=InlineKeyboardButton(text='Киви')
f6=InlineKeyboardButton(text='Нектарины')
f7=InlineKeyboardButton(text='Грейпфрукт')
f8=InlineKeyboardButton(text='Апельсины')
f9=InlineKeyboardButton(text='Лимоны')
f10=InlineKeyboardButton(text='Мандарины')
fruit.add(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10)