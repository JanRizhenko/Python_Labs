N = int(input("Введіть ціле число N (> 1): "))

if N > 1:
    K = 0
    power_of_5 = 1
    while power_of_5 <= N:
        K += 1
        power_of_5 = 5 ** K
    print("Найменше ціле число K, при якому 5^K > N:", K)
else:
    print("Помилка: значення N повинно бути більше 1.")