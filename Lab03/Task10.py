text = "Now the new product was launched. It’s not expected to be popular, but people appreciate novelty."
print("Початковий текст:\n", text, "\n")

letter_n = input("Введіть літеру, з якої починаються слова (N): ").lower()
letter_p = input("Введіть літеру, на яку закінчуються слова (P): ").lower()

words = text.split()
start_with_n = [word for word in words if word.lower().startswith(letter_n)]
end_with_p = [word for word in words if word.lower().endswith(letter_p)]

print("\nСлова, що починаються на", letter_n.upper() + ":", start_with_n)
print("Слова, що закінчуються на", letter_p.upper() + ":", end_with_p, "\n")