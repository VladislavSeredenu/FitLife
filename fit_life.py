# Проект FitLife - MVP версия 1.0

#Функция для подсчета ИМТ.
def body_index(weight, height):
    if height <= 0:
        raise ValueError("Рост не может быть меньше нуля!")
    return weight / (height ** 2)

#Функция измеряет норму воды в день.
def water_balance(weight):
    if weight < 0:
        raise ValueError("Вес не может быть отрицательным!")
    ml_per_kg = 30
    return (weight * ml_per_kg) / 1000

#Функция спасает от ошибки при вводе буквы вместо цифры.
def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Ой, похоже, ты ввёл не число! Попробуй ещё раз, пожалуйста.")

#Проверка пользователь или PyTest.
if __name__ == "__main__":
    print("Привет! Я бот FitLife. Давай составим твой персональный отчёт!\n")

#Бесконечный цикл написан для ловли ошибок при вводе буквы вместо цифр.
    while True:
        try:
            name_user = input("Как тебя зовут? ").strip()
            if not name_user:
                print("Имя не может быть пустым. Попробуй ещё раз.")
                continue

#3 раза Input  показывает ниже, тест пай его не видит, так как там просит именно чистый input
            year_user = get_float_input("Сколько тебе лет? ")
            weight_user = get_float_input("Введи свой вес (в кг): ")
            height_user = get_float_input("Введи свой рост (в метрах, например 1.70): ")

            bmi = body_index(weight_user, height_user)
            water = water_balance(weight_user)

            separator = "=" * 40
            print()
            print(separator)
            print(f"Отчёт для пользователя: {name_user} {int(year_user)} г.")
            print(f"Твой Индекс Массы Тела: {bmi:.1f}")
            print(f"Рекомендуемая норма воды: {water:.1f} л. в день")
            print("=" * 40)
            print("Расчет окончен. Будьте здоровы!")

            break

#Если рост <=0 команда начнет сначала, а также вес <=0.
        except ValueError as e:
            print(f"\nОшибка в данных: {e}")
            print("Давай попробуем ещё раз с самого начала.\n")
