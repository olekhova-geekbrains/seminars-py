from time import perf_counter
from random import randint

def unique_set(lst: list):
    unique = set()
    not_unique = set()
    for el in lst:
        if el in unique:
            unique.remove(el)
            not_unique.add(el)
        elif el not in not_unique:
            unique.add(el)
    return list(unique)


def unique_list1(lst: list):
    rez = []
    for el in lst:
        if lst.count(el) == 1:
            rez.append(el)
    return rez


def unique_list2(lst: list):
    return [el for el in lst if lst.count(el) == 1]




if __name__ == "__main__":
    # lst = [1, 2, 3, 1, 5, 7, 2, 3, 4, 1, 9]  # [4,5,7,9]
    # lst = [1, 2, 3, 5, 1, 5, 3, 10, 1]

    lst = [randint(1,15) for _ in range(1000)]

    t1 = perf_counter()
    print(unique_set(lst))
    t2 = perf_counter()
    print(unique_list1(lst))
    t3 = perf_counter()
    print(unique_list2(lst))
    t4 = perf_counter()


    print(f"set: {t2-t1:.2e}; list: {t3-t2:.2e} comp: {t4-t3:.2e}")

# 100:   set: 4.25e-05; list: 1.33e-04 comp: 1.23e-04
# 1000:  set: 8.94e-05; list: 1.49e-02 comp: 1.39e-02