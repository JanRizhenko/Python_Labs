numbers = [float(input("Число 1:")), float(input("Число 2:")), float(input("Число 3:"))]
result = [num for num in numbers if 1 <= num <= 3]
print("Числа в інтервалі [1, 3]:", result)