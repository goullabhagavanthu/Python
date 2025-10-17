s = {
    'name' : 'GOOG',
    'shares' : 100,
    'price' : 490.10
}

name = s['name']
cost = s['shares'] * s['price']
print(name,cost)

s['shares'] = 75
print(s)
s['date'] = '2007-06-07'
print(s)

prices = {
    'GOOG' : 490.1,
    'AAPL' : 123.5,
    'IBM' : 91.5,
    'MSFT' : 52.13
}

p = prices['IBM']
print(p)

p = prices.get('IBM', 0.0)
print(p)

del prices['GOOG']
print(prices)