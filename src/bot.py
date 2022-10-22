import logging
import os
import ccxt
import argparse

from core.exchange import CryptoExchange
from core.telegrambot import TelegramBot
from core.tradeexecutor import TradeExecutor

from os import getenv

message = 'Please wait while the program is loading...'
print(message)


# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# VAR
telegram_tkn = getenv("TOKEN")
ALLOWED_USER_ID = getenv("ALLOWED_USER_ID")
parser = argparse.ArgumentParser(description="INT Transformation")
parser.add_argument("--user-id", required=False, type=int, default=ALLOWED_USER_ID)
args = parser.parse_args()
user_id = args.user_id

if not user_id:
    logger.warning('user_id not set, you will not be able to control the bot')



exchange_id = getenv("EXCHANGE1")
exchange_id1_api = getenv("EXCHANGE1YOUR_API_KEY")  
exchange_id1_secret = getenv("EXCHANGE1YOUR_SECRET") 

#EXCHANGE
exchange_class = getattr(ccxt, exchange_id)
ccxt_ex = exchange_class({
    'apiKey': exchange_id1_api,
    'secret': exchange_id1_secret,
})


exchange = CryptoExchange(ccxt_ex)
print(exchange.fetch_balance())
print(exchange.free_balance)


trade_executor = TradeExecutor(exchange)


#BOT
telegram_bot = TelegramBot(telegram_tkn, user_id, trade_executor)
telegram_bot.start_bot()

