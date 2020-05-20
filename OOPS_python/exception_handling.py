# Define your exception up here:
class OutOfStock(Exception):
    pass


# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if (self.stock[color] == 0):
            raise OutOfStock
        else:
            self.stock[color] += 1


candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
try:
    candle_shop.buy('blue')
    candle_shop.buy('green')
except OutOfStock:
    print("We are out of stock, please come tomorrow.")