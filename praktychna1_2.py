import math

a = int(input("Введіть катет: "))
c = int(input("Введіть гіпотенузу: "))

b = math.sqrt(c ** 2 - a ** 2)
s = (a * b)/2

print("Площа прямокутного трикутника:", s)