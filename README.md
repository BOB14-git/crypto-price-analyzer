# Real-Time Crypto Analyzer

## Project Overview
A Python program that gives you price details about coins like Bitcoin, Ethereum, and Cardano in real time.

## Project Objectives
1. Tracking coin prices continuously.
2. Saving price data with time and date stamps.
3. Analyzing data and identifying coins with the highest and lowest price changes.

## Features
1. Coin prices in USD.
2. Tracking 24-hour price percentage changes.
3. Saving data in a SQLite database automatically.
4. Calculating Average, Max, and Min prices for each coin.
5. Error handling for network stability.

## Tech Stack
* **Language:** Python 3
* **Database:** SQLite3
* **Libraries:** `urllib`, `json`, `datetime`, `time`, `ssl`

## Database Structure
The project uses a SQLite table named `Prices` with the following columns:
* `id`: Primary key (auto-increment)
* `coin`: Name of the cryptocurrency
* `price`: Current price in USD
* `change_24h`: 24-hour price change percentage
* `timestamp`: Date and time of the record

## How to Run
1. Make sure you have Python 3 installed.
2. Run the script:
   ```bash
   python crypto_analyzer.py
