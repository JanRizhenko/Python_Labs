def is_palindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_palindrome(word[1:-1])
    else:
        return False

word = input("Введіть слово: ")

if is_palindrome(word):
    print(f"Слово '{word}' є паліндромом.")
else:
    print(f"Слово '{word}' не є паліндромом.")
