# Ashton Hollick 11/2024

# initialize price variable and list of valid coins
price = 50
coins = [5, 10, 25]

#using while to keep track of amount paid
while price > 0:
    print(f"Amount Due: {price}")

#getting user input of coin
    paid = int(input("Insert Coin: "))

#check its valid, subtract from price
    if paid in coins:
        price -= paid

# print any change left
print(f"Change Owed: {abs(price)}")