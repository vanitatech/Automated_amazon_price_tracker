from bs4 import BeautifulSoup
import requests
import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

# Step 1: Use beautiful soup to scrape the product price
practice_url = "https://appbrewery.github.io/instant_pot/"
response = requests.get(practice_url, timeout=15)
soup = BeautifulSoup(response.text, "html.parser")

price_element = soup.find(name="span", class_="a-price-whole")
if price_element:
    practice_price = float(price_element.get_text().strip().replace(",", ""))
    print("Practice_price: ", practice_price)

# Step 2 Email alert when the price is below preset value
    preset_price = 160

    if practice_price < preset_price:
        print("Price is below preset value! Send email alert.")
        with smtplib.SMTP("smtp.gmail.com", 587) as connector:
            connector.starttls()
            connector.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
            connector.sendmail(
                from_addr=os.environ["EMAIL_USER"],
                to_addrs=os.environ["EMAIL_USER"],
                msg=f"Subject:Price Alert!\n\nThe price is below {preset_price}."
            )


# Step 3: Add headers to your request
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-GB,en;q=0.9"
}

# Step 4: Scrape the live Amazon site
amazon_url = "https://www.amazon.co.uk/dp/B08HRZBY99"

try:
    response = requests.get(amazon_url, headers=headers, timeout=15)
    print("Amazon status code:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.select_one("#productTitle")
    price = soup.select_one("span.a-price span.a-offscreen")

    if title and price:
        print("Product:", title.get_text(strip=True))

        price_text = (price.get_text(strip=True).replace("£", "").replace(",", ""))
        amazon_price = float(price_text)
        print("Amazon price:", amazon_price)

        # Only compare the real Amazon price here
        if amazon_price < preset_price:
            print("Amazon price is below the preset price!")
            with smtplib.SMTP("smtp.gmail.com", 587) as connector:
                connector.starttls()
                connector.login(os.environ["EMAIL_USER"], os.environ["EMAIL_PASS"])
                connector.sendmail(
                    from_addr=os.environ["EMAIL_USER"],
                    to_addrs=os.environ["EMAIL_USER"],
                    msg=f"Subject:Price Alert!\n\nThe price is below {preset_price}."
                )
    else:
        print("Amazon product details not found.")
        print("Page title:", soup.title.get_text(strip=True) if soup.title else "No title")
        print("No Amazon price alert will be sent.")

except requests.RequestException as error:
    print("Amazon request failed:", error)
