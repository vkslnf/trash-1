a, c, m, l, z = map(int, input().split())
x = 0
n = 0
mas = []
while int(n) != int(z):
    x = (a * l + c) % m
    l = x
    n += 1
    mas.append(x)

answer = (sum(mas) / len(mas))
print("{:.4f}".format(answer))