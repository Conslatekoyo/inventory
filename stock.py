stock={'apples':30, 'oranges':20, 'avocado':5}
alreadyAte={}

food= input('What food was eaten?')
person=input('Who ate the food?')
# stock[food]-=1
# print(f"{person} ate {food}")

if food in stock:
    if person in alreadyAte:
            print('{} was sent to the brig'.format(person))
    stock[food] -=1
    alreadyAte.append(person)
    print('{} ate {}'.format(person,food))
elif:
    stock[food]>0
    stock[food] -=1
    alreadyAte.append(person)
    print("{} ate {}".format(person,food))
else:

    print('{}are out of stock'.format(food))