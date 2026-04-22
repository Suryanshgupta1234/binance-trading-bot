# Binance Futures Testnet Trading Bot

## Features
- Market and Limit order support
- BUY and SELL support
- CLI-based input
- Input validation
- Logging to file (trading.log)
- Order status tracking

## Setup

1. Clone repository
2. Install dependencies:
   pip install -r requirements.txt

3. Create `.env` file:
   API_KEY=your_key
   API_SECRET=your_secret

## Usage

### Market Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

### Limit Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 90000

## Notes
- Uses Binance Futures Testnet (USDT-M)
- Includes post-order status tracking

## Logs
Check `trading.log` for request/response logs