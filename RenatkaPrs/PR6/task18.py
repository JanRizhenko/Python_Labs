a = list(map(int, input("Введіть першу послідовність: ").split()))
b = list(map(int, input("Введіть другу послідовність: ").split()))

common = set(a) & set(b)

print("Числа, що є в обох послідовностях:")
print(' '.join(str(x) for x in a if x in common))
