import csv

def parse_duration(duration_str):
    if "хв" in duration_str and "сек" in duration_str:
        parts = duration_str.split(" ")
        minutes = int(parts[0].replace("хв", ""))
        seconds = int(parts[2].replace("сек", ""))
        return minutes + seconds / 60
    return 0

def safe_float_conversion(value):
    try:
        return float(value.replace(",", "."))
    except ValueError:
        return None

file_name = "marks.csv"
students_data = []
with open(file_name, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        students_data.append(row)

student_ids = {row[0] for row in students_data}
students_count = len(student_ids)

grades_count = {}
for row in students_data:
    grade = safe_float_conversion(row[4])
    if grade is not None:
        grades_count[grade] = grades_count.get(grade, 0) + 1

time_to_grades = {}
for row in students_data:
    duration = parse_duration(row[3])
    grade = safe_float_conversion(row[4])
    if grade is not None:
        rounded_time = round(duration)
        if rounded_time not in time_to_grades:
            time_to_grades[rounded_time] = []
        time_to_grades[rounded_time].append(grade)

average_grades_per_time = {time: sum(grades) / len(grades) for time, grades in time_to_grades.items()}

questions_stats = {}
questions = students_data[0][5:]
for i, question in enumerate(questions):
    correct = sum(1 for row in students_data if safe_float_conversion(row[5 + i]) and safe_float_conversion(row[5 + i]) > 0)
    total = len(students_data)
    questions_stats[f"Question {i + 1}"] = {
        "correct_percent": (correct / total) * 100,
        "incorrect_percent": 100 - (correct / total) * 100,
    }

ratios = []
for row in students_data:
    grade = safe_float_conversion(row[4])
    duration = parse_duration(row[3])
    if grade is not None and duration > 0:
        ratio = grade / duration
        ratios.append((ratio, row[0]))

top_5_ratios = sorted(ratios, reverse=True)[:5]

output_file = "statistics.txt"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(f"Кількість студентів: {students_count}\n")
    file.write("Статистика за оцінками:\n")
    for grade, count in grades_count.items():
        file.write(f"Оцінка {grade}: {count} студентів\n")
    file.write("Середня оцінка за час виконання:\n")
    for time, avg_grade in sorted(average_grades_per_time.items()):
        file.write(f"{time} хв: {avg_grade:.2f}\n")
    file.write("Аналіз правильності відповідей:\n")
    for question, stats in questions_stats.items():
        file.write(f"{question}: Правильно: {stats['correct_percent']:.2f}%, Неправильно: {stats['incorrect_percent']:.2f}%\n")
    file.write("Топ-5 співвідношень оцінка/час:\n")
    for ratio, student_id in top_5_ratios:
        file.write(f"ID {student_id}: {ratio:.2f}\n")
