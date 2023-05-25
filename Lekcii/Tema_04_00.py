'''
Анонимные, lambda-функции
'''
data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data :
    if i % 2 == 0:
        out.append((i, i ** 2))
print(out)
'''
Как можно сделать этот код лучше, используя lambda?
'''
def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
