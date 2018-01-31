def average(*args):
    s = 0
    n = 0
    for x in args:
        s = x + s
        n = n + 1
    if n==0:
        return 0
    return s/n

print(average())
print(average(1, 2))
print(average(1, 2, 2, 3, 4))