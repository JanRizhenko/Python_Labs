users = {
    232: "Alice",
    550: "Bob",
    190: "Jack"
}

ids = list(map(int, input("Введіть ідентифікатори через пробіл: ").split()))

for user_id in ids:
    if user_id in users:
        print(f"Hi, {users[user_id]}!")
    else:
        print("Hi, to all!")
