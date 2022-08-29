amount = input('How much (In cents)? ')
quarter = int(amount) / 25
rem = int(amount) % 25
dime = rem / 10
rem = rem % 10
nickel = rem / 5
penny = rem % 5
print('Quarters:', int(quarter))
print('Dime:', int(dime))
print('Nickel:', int(nickel))
print('Penny:', penny)
