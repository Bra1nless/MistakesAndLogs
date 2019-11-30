d = {"pear": "груша"}

try:
    print(d["apple"])
except KeyError:
    print("Нет такого ключа в словаре. Доступные ключи: ", d.keys())

try:
    fp = open("blabla.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print("File found")