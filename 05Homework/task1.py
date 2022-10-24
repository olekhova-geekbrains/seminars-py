# 1. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, 
# текст исправить, исправленный текст записать в новый файл. 
# Использовать вложенный менеджер контекста

def read_from_file(filename: str) -> str:
    with open(filename, mode="r", encoding="utf-8") as f:
        a = f.read()
    return a
       

def save_to_file(filename: str, text: str):
    with open(filename, mode='w', encoding="utf-8") as f:
        f.write(text)


def remove_words(text: str, rm_txt: str) -> str:
    words = text.split()
    new_words = filter(lambda word: rm_txt not in word, words)
    return ' '.join(new_words)


FINDTXT = "abc"

text_in = read_from_file('file1_in.txt')
text_out = remove_words(text_in, FINDTXT)
save_to_file('file1_out.txt', text_out)
