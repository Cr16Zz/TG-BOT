import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN= '8013882605:AAGU46e77671oTAReCw11btmWPn56SrAERw'
WEATHER_API_KEY= 'b5f99b72d401be7fac1eff9e04c7b8dd'
bot = Bot(token=API_TOKEN)
logging.basicConfig(level=logging.INFO)

dp = Dispatcher(bot)
@dp.message_handler(commands=["Start"])

async def send_welcome(message: types.Message):
    await message.answer("Вы запустили нашего бота!")

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("неизвестная команда, я не понимаю")

@dp.message_handler(commands=weather)
async def echo(message: types.Message):
    await message.answer("неизвестная команда, я не понимаю")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


def get_weather_samara():
    city = "Самара"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        weather_desc = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        city_name = data['name']
        country = data['sys']['country']
        return (
                f"🌤 Погода в {city_name}, {country}:\n"
                f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"Описание: {weather_desc}\n"
                f"Влажность: {humidity}%\n"
                f"Скорость ветра: {wind_speed} м/с"
            )
    else:
        return '❌ Не удалось получить данные о погоде.'