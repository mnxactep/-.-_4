import num2words

def get_currency_ending(number):
    if number % 10 == 1 and number % 100 != 11:
        return "рубль"
    elif number % 10 in [2, 3, 4] and number % 100 not in [12, 13, 14]:
        return "рубля"
    else:
        return "рублей"

def convert_to_words(number):
    words = num2words.num2words(number, lang='ru')
    words = words.replace('-', ' ')
    words = words.replace(',', '')
    words = words.replace(' и', ',')
    words = words.split()

    if number == 1:
        words.append("рубль")
    else:
        words.append(get_currency_ending(number))

    words[0] = words[0].capitalize()

    return ' '.join(words)

input_number = int(input("Введите число от 1 до 100000: "))
print(convert_to_words(input_number))
