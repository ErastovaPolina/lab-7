def punctuation_(data):
    pass


cases = ["Привет, как дела?", "Это тестовая строка! Специально для проверки.", "Знаки препинания: . , ; : ! ? () []", "Нет знаков препинания"]

results = ["Привет как дела", "Это тестовая строка Специально для проверки", "Знаки препинания", "Нет знаков препинания"]


def test_punctuation_(data):

    all_passed = True
    for case, result in zip(cases, results):
        if punctuation_(case) != result:
            all_passed = False

    if all_passed:
        print('YES')
    else:
        print('NO')
