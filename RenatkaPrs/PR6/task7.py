nums = list(map(int, input("Введіть список чисел: ").split()))
greater = [nums[i] for i in range(1, len(nums)) if nums[i] > nums[i - 1]]
print("Елементи, більші за попередній:", *greater)
