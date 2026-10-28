# Amazon Price Tracker

A small Python script that checks a product price and sends an email alert when the price is below a preset amount.

## What it does

- Checks a practice product page at App Brewery and compares its price with the £160 threshold.
- Requests an Amazon UK product page, extracts the product title and price when available, and compares that price with the same threshold.
- Sends an email alert through Gmail when a detected price is below the threshold.
- Prints a message when Amazon product details cannot be found or the request fails.

The current script uses the Amazon product URL and threshold defined directly in `main.py`.

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`
- `python-dotenv`
- A Gmail account configured to send mail using SMTP. Gmail may require an app password.

Install the Python packages:

```bash
pip install requests beautifulsoup4 python-dotenv
```

## Configuration

Create a `.env` file in the project directory and set these environment variables:

```env
EMAIL_USER=your-email@gmail.com
EMAIL_PASS=your-gmail-app-password
```

Keep `.env` private. Do not commit credentials or share them publicly.

## Run

From the project directory, run:

```bash
python main.py
```

The script prints the prices and status messages to the terminal. If a price is below the threshold, it sends an email to the address in `EMAIL_USER`.

## Notes

- Amazon may change its page markup, block automated requests, or return a page without product details. In those cases, the script cannot extract the price and will print a message instead.
- The practice-page check and the Amazon check both use the same threshold. The practice check may send an alert independently of the Amazon check.
