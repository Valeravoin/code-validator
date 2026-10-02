import math

# === ШАГ 1: ВВОД И ОЧИСТКА ===

user_input = input("Введите несколько кодов через запятую (например: abc123, test_99, qwerty): ")

code_list = user_input.split(",")
clean_list = []

for i in code_list:
    cleaned_item = i.strip()
    clean_list.append(cleaned_item)

# === ШАГ 2: ВАЛИДАЦИЯ КОДОВ ===

valid_codes = []
invalid_codes = []

for j in clean_list:
    has_digit = False

    # Проверяем: длина 4-12, не начинается/не заканчивается на '_', нет пробелов
    if (
        4 <= len(j) <= 12
        and not j.startswith("_")
        and not j.endswith("_")
        and " " not in j
    ):
        # Ищем хотя бы одну цифру
        for char in j:
            if char.isdigit():
                has_digit = True
                break
        if has_digit:
            valid_codes.append(j)
        else:
            invalid_codes.append(j)
    else:
        invalid_codes.append(j)

# === ШАГ 3: СТАТИСТИКА ===

all_valid_code = len(valid_codes)

longest_lengt = 0
shortest_lengt = 13
longest_code = ""

for code in valid_codes:
    if len(code) > longest_lengt:
        longest_lengt = len(code)
        longest_code = code
    if len(code) < shortest_lengt:
        shortest_lengt = len(code)

total_digits_sum = 0
for code in valid_codes:
    for char in code:
        if char.isdigit():
            total_digits_sum += int(char)

# === ШАГ 4: ГЕНЕРАЦИЯ «ИДЕАЛЬНОГО» КОДА ===

if len(valid_codes) > 0:
    prefix = longest_code[:3]

    digit_part = "0"
    for char in longest_code:
        if char.isdigit():
            digit_part = char
            break

    special_char = chr(ord("z") + 1)
    final_code = prefix + digit_part + special_char

# === ШАГ 5: ВЫВОД ОТЧЁТА ===

if len(valid_codes) == 0:
    print(
        "\n⚠️ Валидных кодов не найдено. Невозможно сгенерировать идеальный код и посчитать статистику."
    )
else:
    print("--- Отчёт по валидации кодов ---")
    print(f"Всего введено кодов: {len(clean_list)}")
    print(f"Прошли проверку: {all_valid_code}")
    validity_percent = (
        (all_valid_code / len(clean_list)) * 100 if len(clean_list) > 0 else 0
    )
    print(f"Процент валидных кодов: {validity_percent:.2f}%")

    avg_length = (
        sum(len(code) for code in valid_codes) / len(valid_codes)
        if len(valid_codes) > 0
        else 0
    )

    print(f"\nСтатистика длин валидных кодов:")
    print(f"Минимальная длина: {shortest_lengt}")
    print(f"Максимальная длина: {longest_lengt}")
    print(f"Средняя длина: {avg_length:.2f}")

    sqrt_sum = math.sqrt(total_digits_sum)
    print(f"\nСумма всех цифр в валидных кодах: {total_digits_sum}")
    print(f"Квадратный корень из суммы: {sqrt_sum:.2f}")

    print(f"\nСгенерированный «идеальный» код: {final_code}")
    print(
        "Состав: первые 3 символа самого длинного валидного кода + первая найденная цифра + спецсимвол после 'z' в Unicode."
    )

    print(f"\nПримеры валидных кодов (всего {len(valid_codes)}):")
    if len(valid_codes) <= 5:
        print(*valid_codes, sep=", ")
    else:
        print(*valid_codes[:5], sep=", ", end="")
        print(f", и ещё {len(valid_codes) - 5} кодов")

    print(f"Примеры невалидных кодов (всего {len(invalid_codes)}):")
    if len(invalid_codes) <= 5:
        print(*invalid_codes, sep=", ")
    else:
        print(*invalid_codes[:5], sep=", ", end="")
        print(f", и ещё {len(invalid_codes) - 5} кодов")

    print("\nПравила валидации:")
    print("- Длина кода: от 4 до 12 символов")
    print("- Не должен начинаться или заканчиваться на символ '_'")
    print("- Внутри не должно быть пробелов")
    print("- Должен содержать хотя бы одну цифру")
