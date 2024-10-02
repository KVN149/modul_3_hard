def calculate_structure_sum(*args):
    s= 0
    for item in args:
        if isinstance(item, list): # список []
            for i in item:
                s += calculate_structure_sum(i)
        elif isinstance(item, tuple): # кортеж ()
            for i in item:
                s += calculate_structure_sum(i)
        elif isinstance(item, set): # множества {}
            for i in item:
                s += calculate_structure_sum(i)
        elif isinstance(item, dict): # словарь { a:1, b:2}
            for key, value in item.items():
                s += calculate_structure_sum(key, value)
        elif isinstance(item, str): # строка ' '
            s += len(item)
        elif isinstance(item, int): # число
            s += item
    return s


data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)


