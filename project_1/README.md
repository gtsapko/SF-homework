# My Data Science Project
From the [SkillFactory Data Science Course](https://skillfactory.ru/data-science-specialization).

## Проекты
- [Проект 0: Игра угадай число](https://github.com/gtsapko/SF-homework/tree/main/project_0)
- [Проект 1: Игра угадай число за 20 попыток](https://github.com/gtsapko/SF-homework/tree/main/project_1)

## Оглавление
[1. Описание проекта](https://github.com/gtsapko/SF-homework/tree/main/project_0/README.md#описание-проекта)
[2. Какой кейс решаем?](https://github.com/gtsapko/SF-homework/tree/main/project_0/README.md#какой-кейс-решаем)
[3. Этапы работы над проектом](https://github.com/gtsapko/SF-homework/tree/main/project_0/README.md#этапы-работы-над-проектом)
[4. Результаты](https://github.com/gtsapko/SF-homework/tree/main/project_0/README.md#результаты)


### Описание проекта
Нужно написать программу которая угадывает число за 20 попыток или меньше

### Какой кейс решаем?

- Компьютер загадывает целое число от 1 до 100, и нам его нужно угадать. Под «угадать», подразумевается «написать программу, которая угадывает число».    
- Алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток. 


### Этапы работы над проектом

Сначала устанавливаем любое случайное число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
В цикле берем следующее число как середину интервала между большим и меньшим числом (predict_number = (max_number + min_number) // 2)
Функция score_game подсчитывает количество попыток за которое программа угадала число

### Результаты
По результатам тестов алгоритм угадывает число в среднем за:6 попыток


#### Ссылка на результаты
[Результаты](https://docs.google.com/document/d/1uEg1jOI9doD5RUiEOJVMrqeHXDxrIdxyfsgCNT3MQFY/edit?usp=sharing)