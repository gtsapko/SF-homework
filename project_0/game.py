"""Игра угадай число"""
import numpy as np

number = np.random.randint(1, 101) # загадываем число от 1 до 100

count = 0 # счетчик числа попыток угадывания

while True:
    count += 1
    predict_number = int(input("Угадай число от 1 до 100 "))
    
    if predict_number > number:
        print("Число должно быть меньше")
        
    elif predict_number < number:
        print("Число должно быть больше")
        
    else:
        print(f"Вы угадали это число = {number}, за {count} попыток")
        break # конец игры и выход из цикла