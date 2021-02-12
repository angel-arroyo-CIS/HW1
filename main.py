print('Enter amount of lemon juice (in cups):')
LemonJuice = float(input())

print('Enter amount of water (in cups):')
Water = float(input())

print('Enter amount of agave nectar (in cups):')
AgaveNectar = float(input())

print('How many servings does this make?')
Servings = float(input())


print('\nLemonade ingredients - yields', '{:.2f}'.format(Servings), 'servings')
print('{:.2f}'.format(LemonJuice), 'cup(s) lemon juice')
print('{:.2f}'.format(Water), 'cup(s) water')
print('{:.2f}'.format(AgaveNectar), 'cup(s) agave nectar')

print('\nHow many servings would you like to make?')
Servings2 = float(input())
print('\nLemonade ingredients - yields', '{:.2f}'.format(Servings2), 'servings')
print('{:.2f}'.format(LemonJuice*(Servings2/Servings)), 'cup(s) lemon juice')
print('{:.2f}'.format(Water*(Servings2/Servings)), 'cup(s) water')
print('{:.2f}'.format(AgaveNectar*(Servings2/Servings)), 'cup(s) agave nectar')

print('\nLemonade ingredients - yields', '{:.2f}'.format(Servings2), 'servings')
print('{:.2f}'.format((LemonJuice*(Servings2/Servings))/16), 'gallon(s) lemon juice')
print('{:.2f}'.format((Water*(Servings2/Servings))/16), 'gallon(s) water')
print('{:.2f}'.format((AgaveNectar*(Servings2/Servings))/16), 'gallon(s) agave nectar')