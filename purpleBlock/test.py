# Question
# if this a list of prices [5,2,1,6,9,7] and you have to create a function
# which will give me the best buy price and the best sell prices (1 and 9) to maximise my profit


def best_buy_sell(prices):
    # checking whether length of an array
    if not prices or len(prices) < 2:
        return None

    buy = prices[0]
    sell = prices[1]
    profit = sell - buy
    min_price = buy

    for price in prices[1:]:
        if price - min_price > profit:
            profit = price - min_price
            buy = min_price
            sell = price
        if price < min_price:
            min_price = price

    if profit > 0:
        return buy, sell
    else:
        return None


prices = [5, 2, 1, 6, 9, 7]

result = best_buy_sell(prices)

if result:
    buy_price, sell_price = result
    print("Buy:", buy_price)
    print("Sell:", sell_price)
else:
    print("No profit.")
