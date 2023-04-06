import requests
from bs4 import BeautifulSoup

# Send a request to the website
#url = 'https://www.memoryc.com/39600-amd-ryzen-7-5700x-3-4-ghz-8-core-am4-desktop-cpu-processor.html'
url = 'https://www.memoryc.com/search.html?q=amd+ryzen+7+5700x'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the element with the id 'priceContainer'
price_container = soup.find('div', {'id': 'priceContainer'})

# Get the text attribute of the element and print it
price = price_container.text.strip()

def parsePrice(price):
    comma = False
    price_string = ""

    for i in range(0, len(price)):
        # Find first dollar sign.
        if price[i] == '$':
            # Position pointer two indexes away from dollar sign.
            price_index = i + 2
            while True:
                if price[price_index] != '.':
                    price_string += price[price_index]
                    price_index += 1
                else:
                    price_string += (price[price_index] + price[price_index + 1] + price[price_index + 2])
                    break
    answer = float(price_string)
    return answer


print(parsePrice(price))
