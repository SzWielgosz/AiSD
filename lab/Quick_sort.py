def quick_sort(tab):
    i = len(tab)
    if i <= 1:
        return tab
    else:
        x = tab.pop()

    higher = []
    lower = []
    for i in tab:
        if i > x:
            higher.append(i)
        else:
            lower.append(i)

    return quick_sort(lower) + [x] + quick_sort(higher)


tab = [7, 5, 3, 2, 4, 6, 7, 8, 0, 4, 3]
print(quick_sort(tab))
