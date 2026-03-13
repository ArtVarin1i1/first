#узнать тип данных, int, str и тд вместе с выводом
#age = 3

#print(age, type(age), "\n")
#print("helloworld\n")

#name = input("какое твое имя/возраст: ")
#print("твое имя/возраст: ", int(name), type(int(name)))
'''
a = input("ферст намбер")
b = input("second nuimber")
a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)
result = a / b
print(type(result))
print(result)

'''

'''
a = True
b = False

print(not a)
print(a and b)
print(a or b)
a = 10
print(a > 100)
print(a < 100)
print(a <= 100)
print(a >= 100)
print(a == 100)
print(a != 100)
'''
'''
brand = "volvo"
engine = 1.5
power = 79
sunroof = False
n = int(input('скок у тя мощности: ' ))

if n < 80:
    print("говнище")
else:
    print("имба")
if power < 80:
    print("хуйня")
else:
    print("норм")
    '''
'''
n = int(input("скок лошадкиных сил: "))
if n < 80:
    tax = 0
elif n < 100:
    tax = 10000
elif n < 150:
    tax = 230000
else:
    tax = "дурачина"
print(tax)
'''

'''
brand = "leksus"
engine = 1.5
power = 152
roof = False
n = str(input("естть ли крутая крыша?  "))
car = 0
car = "имба тачка" if n == "да" else "говно"
print(car)
'''
'''
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
'''
"""
i = 0
while i <= 10:
    print(i)
    i = i + 1
    if i == 7:
        break
    elif i < 3:
        continue
"""