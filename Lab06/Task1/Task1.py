with open("numbers.txt", "w") as file:
    for number in [5, 356, 12, -120, -25, -37, 35, 40, 45, 50]:
        file.write(f"{number}\n")

with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]
    total_sum = sum(numbers)

print(f"Сума чисел: {total_sum}")

with open("sum_numbers.txt", "w") as file:
    file.write(f"{total_sum}")