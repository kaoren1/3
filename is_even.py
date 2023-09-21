number = float(input("Введите число: "))
def is_even(number):
    ans = number % 2
    if ans == 0:
        r = True
    else:
        r = False
    return r

number = is_even(number)
print(number)