def calculate_structure_sum(list_):
    summ=0
    for i in list_:
        types=type(i)
        if isinstance(i,int):
            summ += i
        elif isinstance(i,str) :
            summ += len(i)
        elif isinstance(i,list):
            summ += calculate_structure_sum(i)
        elif isinstance(i,dict):
            summ += calculate_structure_sum(list(zip(i.keys(), i.values())))
        elif isinstance(i,tuple ):
            summ += calculate_structure_sum(list(i))
        elif isinstance(i, set):
            summ += calculate_structure_sum(list(i))
    return summ

data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
