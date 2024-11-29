import os
import time
from collections import Counter

input_file = "python.txt"

output_file = f"analysis_results_{time.strftime('%Y%m%d_%H%M%S')}.txt"

def analyze_text(file_path):
    start_time = time.time()

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    letters = Counter(c.lower() for c in text if c.isalpha())

    words = Counter(word.lower() for word in text.split())

    end_time = time.time()
    elapsed_time = end_time - start_time

    results = [
        f"Analysis performed on: {time.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Time taken for analysis: {elapsed_time:.2f} seconds",
        "\nLetter Frequency:",
        *[f"{letter}: {count}" for letter, count in letters.most_common()],
        "\nWord Frequency:",
        *[f"{word}: {count}" for word, count in words.most_common(20)]  # Top 20 words
    ]

    with open(output_file, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(results))

    return results, output_file

analysis_results, result_file_path = analyze_text(input_file)

print("\n".join(analysis_results))


print(f"\nResults saved to: {result_file_path}")
