price = 50
credits = 0

while credits < price:
    coin = int(input('Insert Coin: '))

    if coin == 25 or coin == 10 or coin == 5:
        credits += coin

    if credits < price:
        print('Amount Due: ' + str(price - credits))

print('Change Owed: ' + str(credits - price))