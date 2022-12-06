import joblib
import telebot

API_TOKEN = "5941423926:AAHBf1l-NeqRrnd8_ZU-1s0a1txpJFtwW6k"

model = joblib.load('model.ai')


bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler()
def index(message):
    print(message)
bot.infinity_polling()