filename = 'portfolio.csv'

portfolio = []
with open(filename)as file:
    for line in file:
        row = line.split(',')
        name = row[0]
        shares = int(row[1])
        price = float(row[2])
        holding = (name, shares , price)
        portfolio.append(holding)
        