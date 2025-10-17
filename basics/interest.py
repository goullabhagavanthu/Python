Principal = 1000           # Initial amount
rate = 0.05                   # Interest rate
numyears = 5              # Number of years
year = 1 
while year <= numyears:
    Principal = Principal * (1 + rate)
    print(f'{year:<3d} {Principal:0.2f}')
    year += 1
