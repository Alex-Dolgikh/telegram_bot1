import os, logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

TOKEN = os.getenv('TOKEN') 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}!\nНапиши мне ФИО, или другой текст, например, название компании, и я верну его написание на латинице в соответствии с Приказом МИД России от 12.02.2020 № 2113.'
    logging.info(f'{user_name}({user_id}) sent thr following message:{message.text}')
    await message.reply(text)

@dp.message_handler()
async def send_transcription(message: types.message):
    user_name = message.from_user.first_name
    user_id = message.from_user.id
    letter_dict = {
        'а':'a',
        'б':'b',
        'в':'v',
        'г':'g',
        'д':'d',
        'е':'e',
        'ё':'e',
        'ж':'zh',
        'з':'z',
        'и':'i',
        'й':'i',
        'к':'k',
        'л':'l',
        'м':'m',
        'н':'n',
        'о':'o',
        'п':'p',
        'р':'r',
        'с':'s',
        'т':'t',
        'у':'u',
        'ф':'f',
        'х':'kh',
        'ц':'ts',
        'ч':'ch',
        'ш':'sh',
        'щ':'shch',
        'ы':'y',
        'ъ':'ie',
        'э':'e',
        'ю':'iu',
        'я':'ia',
        'ь':'',
    }
    text = message.text
    try:
        for letter in text: 
            if letter.lower() in letter_dict:
                if letter.islower():
                    text = text.replace(letter,letter_dict[letter])
                else: 
                    text = text.replace(letter,letter_dict[letter.lower()].upper())
            else:
                continue
    except: 
        text = 'Я не справился! Возможно в имени были недопустимые символы. \nПопробуйте еще раз!'
    logging.info(f'{user_name}({user_id}) sent thr following message:{message.text}')
    await bot.send_message(user_id, text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
