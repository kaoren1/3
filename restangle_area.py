width = float(input("Введите ширину: "))
length = float(input("Введите длину: "))
def restangle_area(width, length):
    S = width * length
    return S

x = restangle_area(width, length)
print("Площадь: ", x)