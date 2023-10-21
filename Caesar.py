alphabet_low = list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
alphabet_cap = list("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
symbols = list(' 0123456789`~!@#$%^&*()-_=+\|/[]}{;:<>,.?№"')

while True:
    phrase = input("Введите фразу для зашифровки/расшифровки на русском языке: ")
    flag = True
    for char in phrase:
        if char not in alphabet_low and char not in alphabet_cap and char not in symbols:
            flag = False
            break
    if not flag:
        print("Ваша фраза содержит буквы, не входящие в русский алфавит. Программа не может работать с такими данными.")
    else:
        break

while True:
    shift = int(input("Введите шаг сдвига от -33 до 33 (отрицательные значения - расшифровка; положительные - зашифровка; -33, 33 и 0 не изменят фразу): "))
    if abs(shift) <= 33:
        break
    else:
        print("Введённое число не входит в диапазон от -33 до 33. Попробуйте ещё раз.")

result = ''

for char in phrase:
    if char in alphabet_low:
        index = alphabet_low.index(char)+shift
        if index >= 32:
            index -= 33
        char = alphabet_low[index]
        result += char
    elif char in alphabet_cap:
        index = alphabet_cap.index(char)+shift
        if index >= 32:
            index -= 33
        char = alphabet_cap[index]
        result += char
    else:
        result += char

print(f"Результат: {result}")