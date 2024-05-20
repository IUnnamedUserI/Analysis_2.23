#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import threading

"""
Задача:
С использованием многопоточности для заданного значения найти
сумму ряда с точностью члена ряда по абсолютному значению и
произвести сравнение полученной суммы с контрольным значением функции
для двух бесконечных рядов.
"""

e = 10e-7
stepArray = [1]


def calculateY(x):
    return 0.5 * math.log((x + 1) / (x - 1))


def calculate_step(step, index, x, n):
    step[index] = 1

    def firstStep():
        step[index] *= (2 * n - 1)

    def secondStep():
        step[index] *= x**(2 * n - 1)

    def thirdStep():
        step[index] **= -1

    firstThread = threading.Thread(target=firstStep)
    secondThread = threading.Thread(target=secondStep)
    thirdThread = threading.Thread(target=thirdStep)

    firstThread.start()
    secondThread.start()
    thirdThread.start()

    firstThread.join()
    secondThread.join()
    thirdThread.join()


def main():
    x = 3
    index = 0

    while abs(stepArray[index]) > e:
        stepArray.append(0)
        calculate_step(stepArray, index + 1, x, index + 1)
        index += 1

    S = sum(stepArray) - 1
    y = calculateY(x)

    print(f"\nРезультат при x = {x}")
    print(f"Сумма = {round(S, 4)}")
    print(f"Y = {round(y, 4)}")
    print(f"Разница между S и Y: {abs(round(S - y, 4))}\n")


if __name__ == "__main__":
    main()
