n = int(input("Введіть число n: "))

current = 1  # Починаємо з першого числа
k = 1        # Індекс числа, що буде обчислюватися

while current <= n:
    k += 1
    current = k * k + k

print("Перше число більше n:", current,"\nЧисло, що більше за n за формулою i*i+i: ",k)