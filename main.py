#load_env
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from coingecko_sdk import AsyncCoingecko
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
COIN_GECKO_KEY = os.getenv("COIN_GECKO_KEY")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
coin_gecko = AsyncCoingecko(demo_api_key = "COIN_GECKO_KEY", environment="demo")


#i am getting price of token using coin gecko i have gotten for  i want to get price for bnb and sol and eth
async def btc_price(update:Update, context:ContextTypes.DEFAULT_TYPE):
    price = await coin_gecko.simple.price.get(ids='bitcoin', vs_currencies='usd')

    print(price)

    # {'bitcoin': PriceGetResponseItem(last_updated_at=None, usd=76423.0, usd_24h_change=None, usd_24h_vol=None, usd_market_cap=None)}
    await update.message.reply_text(f"Bitcon price is ${price['bitcoin'].usd}")

async def eth_price(update:Update, context:ContextTypes.DEFAULT_TYPE):
    price = await coin_gecko.simple.price.get(ids='ethereum', vs_currencies='usd')

    await update.message.reply_text(f"Etherum price is ${price['ethereum'].usd}")


async def sol_price(update:Update, context:ContextTypes.DEFAULT_TYPE):
    price = await coin_gecko.simple.price.get(ids='solana', vs_currencies='usd')
    await update.message.reply_text(f"solana price is ${price['solana'].usd}")


async def bnb_price(update:Update, context:ContextTypes.DEFAULT_TYPE):
    price = await coin_gecko.simple.price.get(ids='binancecoin', vs_currencies='usd')

    await update.message.reply_text(f"Binance Coin price is ${price['binancecoin'].usd}")

    
if __name__ == '__main__':
    
    # # Add a handler to listen for the /start command
    # start_handler = CommandHandler('start', start)

    #state the command and the fuction that would run when the command is called
    get_price_btc = CommandHandler('BTC', btc_price)
    get_price_ether = CommandHandler('ETH', eth_price)
    get_price_sol = CommandHandler('SOL', sol_price)

    get_price_bnb = CommandHandler('BNB',bnb_price)
    

    #add the command to the app

    app.add_handler(get_price_btc)
    app.add_handler(get_price_ether)
    app.add_handler(get_price_sol)
    app.add_handler(get_price_bnb)

    
    # Run the bot until you press Ctrl-C
    app.run_polling()


