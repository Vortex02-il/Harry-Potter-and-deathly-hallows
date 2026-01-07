import pygame
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
def in_equilateral_triangle(x, y, n, f):
    x_top = (n - f) // 2
    y_center = (n - 1) // 2
    rel_x = x - x_top
    if 0 <= rel_x < f:
        if abs(y - y_center) <= rel_x:
            return True
    return False
def draw_symbol(n, R, d, language):
    c = n // 2
    for i in range(n):
        line = []
        for j in range(n):
            symbol = "."
            if in_equilateral_triangle(i, j, n, d):
                symbol = "!"
            if (abs(j - c) ** 2 + (1.5 * abs(i - c)) ** 2 <= R * R and
                    abs(j - c) ** 2 + (1.5 * abs(i - c)) ** 2 > (R // 2) ** 2):
                symbol = "#"
            if j == c and in_equilateral_triangle(i, j, n, d):
                symbol = "**"
            line.append(symbol)
        print(' '.join(line))
    if language == "rus":
        input("Вот мы и сделали значок даров Смерти. Чтобы закончить программу нажмите Enter.")
    else:
        input("Now we have the Deathly Hallows icon. To end the program, press Enter.")
g = input("Выберите язык русский напишите Р/ Select English language by pressing E: ")
if g.upper() in ["P", "Р", "R"]:
    print(
        """Вы находитесь в мире Гарри Поттера. И в последней части была одна из главных тем про Дары смерти. Так давайте сделаем этот знак. Поехали!""")
    lang = "rus"
elif g.upper() in ["E", "Е"]:
    print(
        """You're in the world of Harry Potter. And the last installment had one of the main themes: the Deathly Hallows. So let's make this sign. Let's go!""")
    lang = "eng"
else:
    print("Defaulting to English / По умолчанию английский")
    print("""You're in the world of Harry Potter. And the last installment had one of the main themes: the Deathly Hallows. So let's make this sign. Let's go!""")
    lang = "eng"
while True:
    n = int(input("Введите сторону квадрата: " if lang == "rus" else "Enter square side: "))
    R = int(input("Введите радиус камня: " if lang == "rus" else "Enter stone radius: "))
    d = int(input("Введите длину стороны мантии: " if lang == "rus" else "Enter cloak length: "))
    if n > d and R * 2 - 12 < d:
        draw_symbol(n, R, d, lang)
        break
    else:
        if lang == "rus":
            print("Некорректные параметры! Попробуйте снова.")
        else:
            print("Invalid parameters! Try again.")