import matplotlib.pyplot as plt


def getSortedArray(d):
    list_d = list(d.items())
    list_d.sort(key=lambda i: i[1])
    return [i[0] for i in list_d]


def count_bigrams(text):
    res = {}
    for i in range(len(text) - 1):
        if text[i].isalpha() and text[i + 1].isalpha():
            bigram = text[i] + text[i + 1]
            if bigram in res:
                res[bigram] += 1
            else:
                res[bigram] = 1

    res = list(reversed(getSortedArray(res)))
    return res[:11]


def count_trigrams(text):
    res = {}
    for i in range(len(text) - 2):
        if text[i].isalpha() and text[i + 1].isalpha() and text[i + 2].isalpha():
            trigram = text[i] + text[i + 1] + text[i + 2]
            if trigram in res:
                res[trigram] += 1
            else:
                res[trigram] = 1

    res = list(reversed(getSortedArray(res)))
    return res[:6]


def decrypt(text, letterFreq):
    current_chars = {}  # частоты букв во входном сообщении
    res = ''  # истоговое сообщение

    count = 0  # количество букв в исходном тексте
    for char in text:
        if char.isalpha() and char == char.lower():
            count += 1
            if char in current_chars:
                current_chars[char] += 1
            else:
                current_chars[char] = 1

    print(current_chars)
    for char in current_chars:  # перевод в проценты
        current_chars[char] = current_chars[char] * 100 / count

    arr1 = list(reversed(getSortedArray(letterFreq)))
    arr2 = list(reversed(getSortedArray(current_chars)))

    sootv = {}  # массив соответствий и его формирование
    for i in range(len(arr2)):
        sootv[arr2[i]] = arr1[i]

    sootv['ю'] = 'т'  # на основе анализа "когда-то"
    sootv['ц'] = 'о'
    sootv['и'] = 'к'
    sootv['ф'] = 'г'
    sootv['я'] = 'д'
    sootv['м'] = 'а'
    sootv['б'] = 'ы'  # дальше просто подстановки, основываясь на биграммах и тексте, уже не вспомню
    sootv['щ'] = 'в'
    sootv['а'] = 'ч'
    sootv['ъ'] = 'н'
    sootv['д'] = 'е'
    sootv['с'] = 'р'
    sootv['ж'] = 'м'
    sootv['в'] = 'щ'
    sootv['й'] = 'с'
    sootv['э'] = 'и'
    sootv['е'] = 'з'
    sootv['л'] = 'ж'
    sootv['н'] = 'я'
    sootv['т'] = 'ю'
    sootv['ь'] = 'л'
    sootv['з'] = 'п'
    sootv['о'] = 'х'
    sootv['к'] = 'й'
    sootv['п'] = 'б'
    sootv['ы'] = 'у'
    sootv['у'] = 'ш'
    sootv['ч'] = 'ь'
    sootv['ш'] = 'ц'

    for char in text:  # замена
        if char.isalpha():
            if char in sootv:
                res += sootv[char]
            else:
                res += char
        else:
            res += char
    return res, sootv, current_chars


def show_result(text, letterFreq, zam, sootv):
    print('Расшифрованный текст: ')
    print(text)

    plt.bar(letterFreq.keys(), letterFreq.values(), width=0.5, color='g')
    plt.show()

    list_d = list(zam.items())
    list_d.sort(key=lambda i: i[1])
    list_d = list(reversed(list_d))

    plt.bar([i[0] for i in list_d], [i[1] for i in list_d], width=0.5, color='g')
    plt.show()

    for i in sootv:
        print(i + ': ' + sootv[i])


plt.close()

with open('rus_text.txt', encoding='utf8') as file:
    C1 = file.read()

with open('eng_text.txt') as file:
    C2 = file.read().lower()

englishLetterFreq = {
    'E': 12.70,
    'T': 9.06,
    'A': 8.17,
    'O': 7.51,
    'I': 6.97,
    'N': 6.75,
    'S': 6.33,
    'H': 6.09,
    'R': 5.99,
    'D': 4.25,
    'L': 4.03,
    'C': 2.78,
    'U': 2.76,
    'M': 2.41,
    'W': 2.36,
    'F': 2.23,
    'G': 2.02,
    'Y': 1.97,
    'P': 1.93,
    'B': 1.29,
    'V': 0.98,
    'K': 0.77,
    'J': 0.15,
    'X': 0.15,
    'Q': 0.10,
    'Z': 0.07
}

russianLetterFreq = {
    'О': 11.18,
    'Е': 8.95,
    'А': 7.64,
    'И': 7.09,
    'Н': 6.78,
    'Т': 6.09,
    'С': 4.97,
    'Л': 4.96,
    'В': 4.38,
    'Р': 4.23,
    'К': 3.30,
    'М': 3.17,
    'Д': 3.09,
    'П': 2.47,
    'Ы': 2.36,
    'У': 2.22,
    'Б': 2.01,
    'Я': 1.96,
    'Ь': 1.84,
    'Г': 1.72,
    'З': 1.48,
    'Ч': 1.40,
    'Й': 1.21,
    'Ж': 1.01,
    'Х': 0.95,
    'Ш': 0.72,
    'Ю': 0.47,
    'Ц': 0.39,
    'Э': 0.36,
    'Щ': 0.30,
    'Ф': 0.21,
    'Ъ': 0.02
}

print(count_bigrams(C1))
print(count_trigrams(C1))
res_rus, rus_sootv, chast = decrypt(C1, russianLetterFreq)
show_result(res_rus, russianLetterFreq, chast, rus_sootv)

# русские самые частые биграммы и триграммы
# СТ, НО, ЕН, ТО, НА, ОВ, НИ, РА, ВО, КО,
# СТО, ЕНО, НОВ, ТОВ, ОВО, ОВА