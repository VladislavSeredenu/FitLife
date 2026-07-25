# Проект FitLife - MVP версия 1.0

# Константы.
WATER_ML_PER_KG = 30
ML_PER_LITER = 1000
MIN_AGE = 1
MAX_AGE = 120
MIN_WEIGHT = 30
MAX_WEIGHT = 120
MIN_HEIGHT = 1.4
MAX_HEIGHT = 2.2
SEPARATOR = "=" * 40

# Константы для сообщений при выводе.
MSG_AGE_RANGE = f"Возраст должен быть от {MIN_AGE} до {MAX_AGE} лет."
MSG_WEIGHT_RANGE = f"Вес должен быть от {MIN_WEIGHT} до {MAX_WEIGHT} кг."
MSG_HEIGHT_RANGE = f"Рост должен быть от {MIN_HEIGHT} до {MAX_HEIGHT} м."
MSG_INVALID_NUMBER = "Ошибка: нужно ввести число! Попробуй ещё раз."
MSG_EMPTY_NAME = "Имя не может быть пустым. Попробуй ещё раз.\n"


def body_index(weight, height):
    """Рассчитывает ИМТ."""
    if height == 0:
        raise ZeroDivisionError("Рост не может быть равен нулю!")
    return weight / (height ** 2)


def water_balance(weight):
    """Рассчитывает норму воды в литрах."""
    return (weight * WATER_ML_PER_KG) / ML_PER_LITER


def run_fitlife(name, age, weight, height):
    """Формирует отчёт из коротких частей."""
    bmi = body_index(weight, height)
    water = water_balance(weight)
    age_int = int(age)
    part_header = f"Отчёт: {name}"
    part_age = f" ({age_int} г.)"
    part_bmi = f"ИМТ: {bmi:.1f}"
    part_water = f"Норма воды: {water:.1f} л/день"

    lines = (
        "",
        SEPARATOR,
        part_header + part_age,
        part_bmi,
        part_water,
        SEPARATOR,
        "Расчёт окончен. Будьте здоровы!",
    )

    return "\n".join(lines)


def get_name():
    """Запрашивает имя, пока оно не будет введено."""
    while True:
        name = input("Как тебя зовут? ").strip()
        if not name:
            print(MSG_EMPTY_NAME)
            continue
        return name


def get_age():
    """Запрашивает возраст с валидацией диапазона."""
    while True:
        try:
            year_value = float(input("Сколько тебе лет? "))
            if not (MIN_AGE <= year_value <= MAX_AGE):
                print(MSG_AGE_RANGE)
                continue
            return year_value
        except ValueError:
            print(MSG_INVALID_NUMBER)


def get_weight():
    """Запрашивает вес с валидацией диапазона."""
    while True:
        try:
            weight_value = float(input("Введи свой вес (в кг): "))
            if not (MIN_WEIGHT <= weight_value <= MAX_WEIGHT):
                print(MSG_WEIGHT_RANGE)
                continue
            return weight_value
        except ValueError:
            print(MSG_INVALID_NUMBER)


def get_height():
    """Запрашивает рост с валидацией диапазона."""
    while True:
        try:
            height_value = float(input("Введи рост (метры, например 1.70):"))
            if not (MIN_HEIGHT <= height_value <= MAX_HEIGHT):
                print(MSG_HEIGHT_RANGE)
                continue
            return height_value
        except ValueError:
            print(MSG_INVALID_NUMBER)


if __name__ == "__main__":
    print("Привет! Я бот FitLife. Давай составим отчёт!\n")

    name_user = get_name()
    age_raw = get_age()
    weight_raw = get_weight()
    height_raw = get_height()

    report = run_fitlife(name_user, age_raw, weight_raw, height_raw)
    print("\n" + report)
