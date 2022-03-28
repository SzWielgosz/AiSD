from typing import List

def sortowanieBabelkowe(li: List[int]) -> List[int]:
    for i in range(len(li)):
        for j in range(len(li)):
            if li[i] < li[j]:
                tmp = li[i]
                li[i] = li[j]
                li[j] = tmp

    return li

def sortowanieWybieranie(li: List[int]) -> List[int]:
    for i in range(len(li)):
        min_index = i
        for j in range(i + 1, len(li) - 1):
            if li[j] < li[min_index]:
                min_index = j

            tmp = li[j]
            li[j] = li[min_index]
            li[min_index] = tmp

    return li


def sortowanieWstawianie(li:List[int]) -> List[int]:
    for i in range(1, len(li) - 1):
        key = li[i]
        j = i - 1
        while j >= 0 and li[i] > key:
            li[j + 1] = li[j]
        j = j - 1
        li[j + 1] = key

    return li




# li: List[int] = [5, 9, 2, 6, 3]
li2: List[int] = [3, 9, 6, 4, 0]
# sortowanieBabelkowe(li)
# print(li)

sortowanieWstawianie(li2)
print(li2)