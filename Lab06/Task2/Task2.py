nums = []
print("Введіть довільну кількість цілих чисел (або введіть 'end' для завершення):")

while True:
    user_input = input()
    if user_input.lower() == "end":
        break
    try:
        num = int(user_input)
        nums.append(num)
    except ValueError:
        print("Будь ласка, введіть ціле число або 'end'.")

print("Введені числа:", nums)

with open("oddOrEven.txt", "w") as file:
    for num in nums:
        if num % 2 == 0: file.write(str(num)+" - Even" + "\n")
        else: file.write(str(num)+" - Odd" + "\n")