'''
price = 100
user_money = float(input("Enter amount of money: "))
price_of_Nintendo = 100
Money = user_money // price
Issufiency_Money = price_of_Nintendo - (user_money % price)

if Money > 0:
    {int(Money)}
    print("can afford  Nintendo wiis.")
else:
    print(f"You need an additional Pesos {Issufiency_Money:.2f}.")

'''
'''
userInput = int(input("Enter a number: "))
sum = 1
for i in range(1, userInput +1):
    sum *=i

    print(sum, "Is the sum of Integer from 1 to", userInput)
'''


x = int(input("Enter number: "))
if x == 0:
    print(x, "is not a valid input.")
else:
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, "is a factor of", x)