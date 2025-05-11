letter = input("Введіть літеру: ").lower()

if letter in 'aeiouаеєиіїоуюя':
    print(f"{letter} is a vowel")
else:
    print(f"{letter} is a consonant")
