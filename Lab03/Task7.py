text = "Простий приклад тексту для заміни літер п на зірочки."
print("Початковий текст:\n", text, "\n")

n = len(text)
half_text = n // 2

modified_text = ''.join(
    '*' if i < half_text and text[i] == 'п' else text[i]
    for i in range(n)
)

print("Результат після заміни літер 'п' на '*':\n", modified_text, "\n")