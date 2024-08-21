a = int(input ("Введіть а: "))

while (a < 1 or a > 100):

    a = int(input ("Введіть ще раз а: "))

b = int(input ("Введіть b: "))

while (b < 1 or b > 100):

    b = int(input ("Введіть ще раз b: "))

if a < b:

    r = (a * 3 - 5) / b

elif a == b:

    r = -4

else:

    r = (a^4 + b) / a

print("Результат обчислення виразу: " , r)