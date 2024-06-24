def getDataPoint(quote):
    """ Return a tuple containing stock name, bid price, ask price, and calculated price """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Return the ratio of price_a to price_b """
    if price_b == 0:
        return None  # Handle division by zero gracefully
    return price_a / price_b

def main():
    """ Main function to demonstrate the usage of getDataPoint and getRatio """
    quotes = [
        {'stock': 'ABC', 'top_bid': {'price': 120}, 'top_ask': {'price': 121}},
        {'stock': 'DEF', 'top_bid': {'price': 95}, 'top_ask': {'price': 96}},
    ]

    for quote in quotes:
        stock, bid_price, ask_price, price = getDataPoint(quote)
        print(f"Stock: {stock}, Bid Price: {bid_price}, Ask Price: {ask_price}, Calculated Price: {price}")

    price_a = quotes[0]['top_bid']['price']
    price_b = quotes[1]['top_bid']['price']
    ratio = getRatio(price_a, price_b)
    print(f"Ratio: {ratio}")

if __name__ == "__main__":
    main()
