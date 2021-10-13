import numpy as np

number = np.random.randint(1, 1001)  # загадываем число


def better_predict(number: int = 1) -> int:
    """Пытаемся угадать менее чем за 20 попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict_min = 0
    predict_max = 1000

    while True:
        count += 1
        predict = int(np.mean(list(range(predict_min, predict_max))))
        if predict + 2 == predict_max:
            predict_max += 1
        if predict > number:
            predict_max = predict
        if predict < number:
            predict_min = predict
        if predict == number:
            break
    return count


# print(f"Число от 1 до 1000000 загаданное компьютером: {number}")
# print(better_predict(number))
