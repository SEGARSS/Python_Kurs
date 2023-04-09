# Сокращённые представления на примере созданной переменной iter
iter = 2
iter += 3 # iter = iter + 3. Это означает 2+3 = 5
print(iter)
iter -= 4 # iter = iter - 4 Это означает 5-4 (так как выше уже получило 5) = 1
print(iter)
iter *= 5 # iter = iter * 5 Это означает 1*5 = 5
print(iter)
iter /= 5 # iter = iter / 5 Это означает 5/5 = 1
print(iter)
iter //= 5 # iter = iter // 5 Это Целочисленное деление 1 // 5 = 0.0
print(iter)
iter %= 5 # iter = iter % 5 Это остаток от деления 0.0 % 5 = 0
print(iter)
iter **= 5 # iter = iter ** 5 Вохвежение в степень. 
print(iter)