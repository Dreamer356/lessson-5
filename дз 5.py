from colorama import init, Fore, Back, Style

# Ініціалізуємо бібліотеку
init(autoreset=True)

# Виведемо список доступних атрибутів та методів
print("Атрибути та методи бібліотеки Colorama:")

# Список атрибутів
print("Атрибути:")
for attr_name in dir(Fore):
    if not attr_name.startswith("__"):
        print(attr_name)

# Список методів
print("Методи:")
from colorama import Fore

print(f"{Fore.RED}Цей текст буде червоним.")
print(f"{Fore.BLUE}Цей текст буде синім.")

from colorama import Back

print(f"{Back.GREEN}Цей текст матиме зелений фон.")
print(f"{Back.YELLOW}Цей текст матиме жовтий фон.")

from colorama import Style

print(f"{Style.BRIGHT}Цей текст буде жирним.")
print(f"{Style.DIM}Цей текст буде темним.")