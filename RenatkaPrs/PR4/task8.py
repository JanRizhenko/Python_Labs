numbers = [1, 5, 8, 10, 7, 4, 6, 3, 9, 2]

even_numbers = [num for num in numbers if num % 2 == 0]

if len(even_numbers) > 0:
    average = sum(even_numbers) / len(even_numbers)
else:
    average = 0

print("Середнє арифметичне парних чисел:", average)
