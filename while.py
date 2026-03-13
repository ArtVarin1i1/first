n = 0
while n <= 10:
    print(n)
    n = n + 1
    if n == 5:
        break

answer = None

while answer != 'volvo':
    answer = input('какая лучшая марка машыны?')
print("ты прав")

i = 0
while i <= 10:
    print(i)
    i = i + 1
    if i == 7:
        break
    elif i < 3:
        continue