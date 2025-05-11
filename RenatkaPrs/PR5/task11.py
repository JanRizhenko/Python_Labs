text = input("Введіть текст: ")
words = text.split()
vowels = "аеєиіїоуюяaeiouyAEIOUYАЕЄИІЇОУЮЯ"

max_vowel_count = 0
max_vowels = ""
position = -1

for i, word in enumerate(words):
    count = sum(1 for c in word if c in vowels)
    if count > max_vowel_count:
        max_vowel_count = count
        max_vowels = word
        position = i + 1

print(f"Слово: '{max_vowels}', голосних: {max_vowel_count}, позиція: {position}")
