# Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

def pred(a, b, c):
    return not(a and b and c) == ((not a) or (not b) or (not c))

my_set = [True, False]

for x in my_set:
    for y in my_set:
        for z in my_set:
            if pred(x, y, z):
                print(x,y,z, 'верно')
            else:
                print(x,y,z,'не верно')