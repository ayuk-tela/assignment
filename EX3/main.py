a = 0
b = 10

while a < b:
    print(a, 'is incremented to ', a + 1)
    a = a + 1
    if a == 10:
        break

for b in range(1, 10):
    if b % 2 != 0:
     print(b)
