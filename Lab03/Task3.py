text = """Тут, де трава росте...
Земля вся вкрита росою.
Небо синє як вода.
І сонце світить нам щораз..."""

print("Текст:\n", text)
count = text.count('.')
text = text.replace('.', '')

print("\nТекст без крапок:\n", text)
print("Кількість видалених символів:", count)