s1 = input("Перший рядок: ")
s2 = input("Другий рядок: ")

if len(s1) > len(s2):
    print(s1)
elif len(s2) > len(s1):
    print(s2)
else:
    print("equally")