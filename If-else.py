price = 2000
budget = int(input('Enter Your budget: '))

if budget<price :
    print("You can't  buy this ")
    print(budget)
elif budget == price :
    print('you can buy this ')
    print(budget)
else :
    print("its okay")
    print(budget)