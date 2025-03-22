import os
from dotenv import load_dotenv
import telebot
from gtts import gTTS
from io import BytesIO
import openai

# Загружаем переменные окружения
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Настраиваем OpenAI
openai.api_key = OPENAI_API_KEY

# Создаём бота
bot = telebot.TeleBot(TOKEN)

# Обрабатываем все входящие сообщения
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    # Получаем ответ от OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    reply_text = response["choices"][0]["message"]["content"]

    # Отправляем текстовый ответ
    bot.send_message(message.chat.id, reply_text)

    # Генерируем голосовой ответ
    tts = gTTS(text=reply_text, lang="ru")
    voice = BytesIO()
    tts.write_to_fp(voice)
    voice.seek(0)
    bot.send_voice(message.chat.id, voice)

# Запускаем бота
bot.polling()