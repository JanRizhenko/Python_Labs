url = input("Введіть URL: ")

resource_name = url.split("/")[-1]

print(f"Назва ресурсу: {resource_name}")