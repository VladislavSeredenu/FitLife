# Проект FitLife - MVP версия 1.0


def body_index(weight, height):
    """Рассчитывает ИМТ."""
    if height <= 0:
        raise ValueError("Рост не может быть меньше нуля!")
    return weight / (height ** 2)


def water_balance(weight):
    """Рассчитывает норму воды в литрах."""
    if weight < 0:
        raise ValueError("Вес не может быть отрицательным!")
    ml_per_kg = 30
    return (weight * ml_per_kg) / 1000


def run_fitlife(name, age, weight, height):
    """Формирует отчёт из коротких частей."""
    bmi = body_index(weight, height)
    water = water_balance(weight)
    age_int = int(age)
    sep = "=" * 40

    # Разобрал код на части, не пропускала проверка.
    part_header = "Отчёт: " + name
    part_age = f" ({age_int} г.)"
    part_bmi = f"ИМТ: {bmi:.1f}"
    part_water = f"Норма воды: {water:.1f} л/день"

    lines = [
        "",
        sep,
        part_header + part_age,
        part_bmi,
        part_water,
        sep,
        "Расчёт окончен. Будьте здоровы!"
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    print("Привет! Я бот FitLife. Давай составим отчёт!\n")

    while True:
        name_user = input("Как тебя зовут? ").strip()
        if not name_user:
            print("Имя не может быть пустым. Попробуй ещё раз.")
            continue

        try:
            age_user = float(input("Сколько тебе лет? "))
            weight_user = float(input("Введи свой вес (в кг): "))
            height_user = float(input("Введи рост (в метрах, например 1.70):"))

            report = run_fitlife(
                name_user,
                age_user,
                weight_user,
                height_user
            )
            print(report)
            break

        except ValueError as e:
            # Вежливое сообщение об ошибке
            print(f"\nОшибка: {e}")
            print("Давай попробуем сначала.\n")
