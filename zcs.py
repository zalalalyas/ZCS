
#TOKEN = '6929570993:AAHGy5i2_BEMyqh5SsdR1CIb8kARjHtn1os'


 #   api_key = '8RPEYWCZRGUCGSQE'


import telebot
import requests

# Your Telegram bot token
TOKEN = '6929570993:AAHGy5i2_BEMyqh5SsdR1CIb8kARjHtn1os'

# Create a bot instance
bot = telebot.TeleBot(TOKEN)

# Function to get live market price from Alpha Vantage
def get_price(asset):
    # Replace 'YOUR_ALPHA_VANTAGE_API_KEY' with your actual Alpha Vantage API key
    api_key = 'TUUUSY584HJAMRRW'
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={asset}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if 'Global Quote' in data:
        price = data['Global Quote']['05. price']
        return price
    else:
        return None

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Market Price Bot. Send me the symbol of a market asset (e.g., currency pair, commodity, stock, cryptocurrency) to get its live market price.")

# Handler for market asset queries
@bot.message_handler(func=lambda message: True)
def send_price(message):
    asset = message.text.upper()
    price = get_price(asset)
    if price is not None:
        bot.reply_to(message, f"The current price of {asset} is {price}")
    else:
        bot.reply_to(message, f"Sorry, unable to retrieve the price for {asset}. Please make sure the asset symbol is valid.")

# Start the bot
bot.polling()
