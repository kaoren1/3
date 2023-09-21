number = int(input("Введите число: "))
def sum_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    return sum

number = sum_digits(number)
print("Сумма цифр: ", number)