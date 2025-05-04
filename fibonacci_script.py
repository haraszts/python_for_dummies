def fibonacci_sor(value_max):
    list = [0,1]
    for i in range(value_max):
        val = list[i] + list[i + 1]
        list.append(val)
    return list
print(fibonacci_sor(9))
