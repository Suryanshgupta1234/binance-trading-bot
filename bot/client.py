import time
from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    client = Client(
        api_key=os.getenv("API_KEY"),
        api_secret=os.getenv("API_SECRET"),
        testnet=True
    )

    # ✅ FIX: sync time with Binance server
    server_time = client.get_server_time()
    system_time = int(time.time() * 1000)
    client.timestamp_offset = server_time['serverTime'] - system_time

    return client