# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# https: // ru.wikipedia.org/wiki/Кодирование_длин_серий
# Создать функцию сжатия строки и функцию восстановления строки.
# Пример:
# ABCDEFGH -> 1A1B1C1D1E1F1G1H -> ABCDEFGH
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR


def encode(text: str) -> str:
    encoding = ''
    length = len(text)
    i = 0
    while i < length:
        count = 1
        while i + 1 < length and text[i] == text[i + 1]:
            count += 1
            i += 1
        encoding += str(count) + text[i]
        i += 1
    return encoding


def decode(text: str) -> str:
    decoding = ''
    length = len(text)
    i = 0
    while i < length:
        num = ''
        while text[i].isdigit():
            num += text[i]
            i += 1
        decoding += text[i]*int(num)
        i += 1
    return decoding


if __name__ == "__main__":
    TEXT_FOR_ENCODE = "WWJJJHDDDDDDDDDDDDDDDDDDDDPPGRRR"
    encoding = encode(TEXT_FOR_ENCODE)
    print(encoding)
    decoding = decode(encoding)
    print(decoding)
