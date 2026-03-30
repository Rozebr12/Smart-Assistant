import datetime as dt
import platform
import sys


def Sloszenie(a, b):
    return a + b

def Vichitanie(a, b):
    return a - b

def Umnoszenie(a, b):
    return a * b

def Delenie(a, b):
    return a / b

print("Введите соотвествущию команду из далее написаных. System-показывает информацию о системе, Time-показывает точное время, Data-показывает точную дату, Calculator-активирует калькулятор")
Destvie = str(input("\nПишите: "))

time = dt.datetime.now()
data = dt.datetime.now()
year = data.year
month = data.month
infoplat = sys.platform
platver = platform.version()

if Destvie == "Calculator":
    try:

        OneNumber = int(input("\nВведите первое число: "))
        TwoNumber = int(input("Введите второе число: "))
        ZnakDestvia = str(input("Введите знак действия: "))

        if ZnakDestvia == "+":
            print(f"\nРезультат: {Sloszenie(OneNumber, TwoNumber)}")

        elif ZnakDestvia == "-":
              print(f"\nРезультат: {Vichitanie(OneNumber, TwoNumber)}")

        elif ZnakDestvia == "*":
              print(f"\nРезультат: {Umnoszenie(OneNumber, TwoNumber)}")

        elif ZnakDestvia == "/":
              print(f"\nРезультат: {Delenie(OneNumber, TwoNumber)}")

        else:
            print("\nНеизвестный знак действия")

    except ValueError:
        print("\nЛучше введите число!")

    except ZeroDivisionError:
        print("\nДеление на ноль!")

elif Destvie == "Time":
    print(f"\nТекущее время: {time}")

elif Destvie == "Data":
    print(f"\nТекущая год: {year}, Месяц: {month}")

elif Destvie == "System":
    print(f"\nОперационная система: {infoplat}, версия операционной системы: {platver}")

else:
    print("\nНеизвестная команда, возможно вы написали команду с маленькой буквы!")

input("\nДля завершения нажмите Enter...")