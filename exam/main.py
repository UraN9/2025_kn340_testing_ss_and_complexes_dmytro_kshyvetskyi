def get_grade(score: int) -> str:
    """
    Функція повертає оцінку залежно від балу.
    :param score: Бал студента (діапазон 0–100).
    :return: Оцінка (A, B, C, D, F).
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"