import csv
from datetime import date


class Person:
    def __init__(self, surname: str, first_name: str, birth_date: str, nickname: str = None):
        if not surname.strip():
            raise ValueError("Прізвище не може бути порожнім.")
        if not first_name.strip():
            raise ValueError("Ім'я не може бути порожнім.")

        self.surname = surname.strip()
        self.first_name = first_name.strip()
        self.nickname = nickname.strip() if nickname else None

        year, month, day = map(int, birth_date.split('-'))
        birth_date_obj = date(year, month, day)

        if birth_date_obj > date.today():
            raise ValueError("Дата народження не може бути в майбутньому.")

        self.birth_date = birth_date_obj

    def get_age(self) -> str:
        today = date.today()
        age = today.year - self.birth_date.year - (
                (today.month, today.day) < (self.birth_date.month, self.birth_date.day)
        )
        return str(age)

    def get_fullname(self) -> str:
        return f"{self.surname} {self.first_name}"


def create_person_from_input_and_save_to_csv(filename):
    print("Введіть дані для створення нового контакту.")
    surname = input("Прізвище: ").strip()
    first_name = input("Ім'я: ").strip()
    birth_date = input("Дата народження (у форматі YYYY-MM-DD): ").strip()
    nickname = input("Псевдонім (необов'язково): ").strip() or None

    try:
        person = Person(surname=surname, first_name=first_name, birth_date=birth_date, nickname=nickname)
        print("\nКонтакт успішно створено!")
        print(f"Повне ім'я: {person.get_fullname()}")
        print(f"Вік: {person.get_age()} років")
        if person.nickname:
            print(f"Псевдонім: {person.nickname}")

        with open(filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["surname", "name", "birth_date", "fullname", "age", "nickname"])

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow({
                "surname": person.surname,
                "name": person.first_name,
                "birth_date": person.birth_date,
                "fullname": person.get_fullname(),
                "age": person.get_age(),
                "nickname": person.nickname or ''
            })

        print("Контакт успішно додано до файлу.")
    except ValueError as e:
        print(f"Помилка: {e}")
    except Exception as e:
        print(f"Невідома помилка: {e}")


if __name__ == "__main__":
    create_person_from_input_and_save_to_csv('contacts.csv')
