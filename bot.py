from dotenv import load_dotenv
import os
import telebot  # Вернём этот импорт обратно!

# Загружаем переменные окружения из .env
load_dotenv()

# Берём API-ключ из .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Вставь сюда свой токен от BotFather
TOKEN = "7597877063:AAE_qD3MKYSmecAG2M_MVPzGSAD4VDqj4oU"



# Создаем экземпляр бота
bot = telebot.TeleBot(TOKEN)

# Проверочная команда /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я твой личный помощник и психолог 😊')
from dotenv import load_dotenv
import os
import telebot

# Загружаем переменные из .env
load_dotenv()

# Берем токен
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Обрабатываем любое сообщение
@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    bot.send_message(message.chat.id, "Привет, Лена! 🌷 Я уже работаю!")

# Запускаем бота
bot.polling()
from dotenv import load_dotenv
import os
import telebot

# Загружаем переменные из .env
load_dotenv()

# Берем токен
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

# Обрабатываем любое сообщение
@bot.message_handler(func=lambda message: True)
def reply_to_message(message):
    bot.send_message(message.chat.id, "Привет, Лена! 🌷 Я уже работаю!")

# Запускаем бота
bot.polling()
