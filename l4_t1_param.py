from sys import argv

script_name, production, rat, bonus = argv

print(f'Итого: {(float(production) * float(rat)) + float(bonus)}')
