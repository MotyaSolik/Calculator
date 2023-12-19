num1 = int(input("Введите первое число"))
num2 = int(input("Введите второе число"))
znak = input("Введите знак (+ - * /)")
if znak == "+" :
    print("Результат:", num1 + num2)
elif znak == "-":
    print("Результат:", num1 - num2)
elif znak == "*":
    print("Результат:", num1 * num2)
elif znak == "/":
    print("Результат:", num1 / num2)
else:
    print("Напишите знак из перечислинных")