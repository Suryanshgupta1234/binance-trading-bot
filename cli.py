import argparse
import time

from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", required=False, help="Required for LIMIT orders")

    args = parser.parse_args()

    setup_logging()

    try:
        # Validate inputs
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Initialize client
        client = get_client()

        # Place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # Print initial response
        print("\n✅ ORDER SUCCESS")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))
        print("Executed Qty:", order.get("executedQty"))
        print("Avg Price:", order.get("avgPrice", "N/A"))

        # Fetch updated status
        time.sleep(2)

        order_status = client.futures_get_order(
            symbol=args.symbol,
            orderId=order["orderId"]
        )

        print("\n🔄 UPDATED STATUS")
        print("Status:", order_status.get("status"))
        print("Executed Qty:", order_status.get("executedQty"))
        print("Avg Price:", order_status.get("avgPrice"))

    except Exception as e:
        print("\n❌ ORDER FAILED:", str(e))


if __name__ == "__main__":
    main()