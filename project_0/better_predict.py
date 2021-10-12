import numpy as np

number = np.random.randint(1, 1001) # загадываем число

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
        #print(list(range(predict_min, predict_max)))
        #print(f"Предполашаемое число {predict}")
        if predict +2 == predict_max:
            predict_max += 1
            #print(f"Добавляем к максимальному порогу +1")
        if predict > number:
            predict_max = predict
            #print(f"Новый максимальный порог {predict_max}, минимальный порог {predict_min}")
        if predict < number:
            predict_min = predict
            #print(f"Новый минимальный порог {predict_min}, максимальный порог {predict_max}")
        if predict == number:
            #print(f"Число угадано: {predict} за {count} раз")
            break
    return count


#print(f"Число от 1 до 1000000 загаданное компьютером: {number}")
#print(better_predict(number))
