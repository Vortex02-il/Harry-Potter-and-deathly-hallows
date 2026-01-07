import pygame
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
def extract_only_digits_simple(text):
    result = ''.join(filter(str.isdigit, text))
    return int(result) if result else 1
def in_equilateral_triangle_contour(x, y, n, f, width=3):
    x_top = (n - f) // 2
    y_center = (n - 1) // 2
    rel_x = x - x_top
    if 0 <= rel_x < f:
        dist_to_center = abs(y - y_center)
        if dist_to_center <= rel_x:
            near_left_edge = abs(dist_to_center - rel_x) < width
            near_right_edge = abs(dist_to_center + rel_x) < width
            near_bottom = rel_x > f - width
            near_top = rel_x < width
            if near_left_edge or near_right_edge or near_bottom or near_top:
                return True
    return False
def draw_symbol(n, R, d, language):
    c = n // 2
    for i in range(n):
        line = []
        for j in range(n):
            symbol = "."
            if in_equilateral_triangle_contour(i, j, n, d):
                symbol = "!"
            if (abs(j - c) ** 2 + (1.5 * abs(i - c)) ** 2 <= R * R and
                    abs(j - c) ** 2 + (1.5 * abs(i - c)) ** 2 > (R // 2) ** 2):
                symbol = "#"
            if j == c and (n - d) // 2 <= i < (n + d) // 2:
                symbol = "**"
            line.append(symbol)
        print(' '.join(line))
    if language == "rus":
        input("Вот мы и сделали значок даров Смерти. Чтобы закончить программу нажмите Enter.")
    else:
        input("Now we have the Deathly Hallows icon. To end the program, press Enter.")
g = input("Выберите язык русский напишите Р/ Select English language by pressing E: ")
if g.upper() in ["P", "Р", "R", "З", "H", "К"]:
    print("""Вы находитесь в мире Гарри Поттера. И в последней части была одна из главных тем про Дары смерти. Так давайте сделаем этот знак. Поехали!""")
    lang = "rus"
elif g.upper() in ["E", "Е", "У", "T"]:
    print("""You're in the world of Harry Potter. And the last installment had one of the main themes: the Deathly Hallows. So let's make this sign. Let's go!""")
    lang = "eng"
else:
    print("Defaulting to English / По умолчанию английский")
    print("""You're in the world of Harry Potter. And the last installment had one of the main themes: the Deathly Hallows. So let's make this sign. Let's go!""")
    lang = "eng"
while True:
    n_input = input("Введите сторону квадрата (минимум 20): " if lang == "rus" else "Enter square side (minimum 15): ")
    R_input = input("Введите радиус камня (минимум 5): " if lang == "rus" else "Enter stone radius (minimum 5): ")
    d_input = input("Введите длину стороны мантии (минимум 13): " if lang == "rus" else "Enter cloak length (minimum 10): ")
    n = extract_only_digits_simple(n_input)
    R = extract_only_digits_simple(R_input)
    d = extract_only_digits_simple(d_input)
    n = max(n, 20)
    R = max(R, 5)
    d = max(d, 13)
    if n < d + 2:
        d = n - 3
    if R * 2 > d:
        R = d // 2 - 1
    if R < 3:
        R = 3
    if n >= 20 and R >= 5 and d >= 13 and n > d and R * 2 < d:
        draw_symbol(n, R, d, lang)
        break
    else:
        n = 20
        R = 7
        d = 15
        if lang == "rus":
            print(f"Некорректные параметры! Используем: квадрат={n}, радиус={R}, мантия={d}")
        else:
            print(f"Invalid parameters! Using: square={n}, radius={R}, cloak={d}")
        draw_symbol(n, R, d, lang)
        break