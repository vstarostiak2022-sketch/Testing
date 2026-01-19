try:
    value = input("Введіть значення: ")
    print(value/value)
except ValueError:
    print("Погане введення...")
except ZeroDivisionError:
    print("Дуже погане введення...")
except TypeError:
    print("Дуже, дуже погане введення…")
except:
    print("Бууу!")
