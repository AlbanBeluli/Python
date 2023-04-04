def sum_list(list1: list):
    counta = 0
    for items in list1:
        counta += items
    return 'This sum is', counta

print(sum_list([1, 2, 3, 4, 15]))
