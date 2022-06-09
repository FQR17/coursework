import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def Function(s,t):
    p1 = 0.023
    p2 = 0.001
    p3 = 0.001
    p4 = 0.005
    p5 = 0.03
    p6 = 0.006
    dgdt = p1 * (s[0] - Gb) - p3*(s[1] - Ib) * s[0] + 0.1
    didt = (p4*(s[0] - p5)) - p6*(s[1] - Ib) + 0.01
    return [dgdt, didt]

def main():
    t = np.linspace(0,3600) # 1 hour = 3600 seconds
    s0 = [Gb, Ib]
    s = odeint(Function,s0,t)
    plt.plot(t,s[:,0],'r--', linewidth=2.0,label="glucose(t)")
    plt.plot(t,s[:,1],'b--', linewidth=2.0,label="insulin(t)")
    plt.xlabel("t (second)")
    plt.ylabel("10^(-1) * mmole/liter (glucose)\n\n10^(-1) * pmol/liter (insulin)")
    plt.legend()
    plt.grid()
    plt.show()

def menu():
    global Gb, Ib

    print("\nЭто программа для решения системы дифференциальных уравнений\n"
          "математической модели гомеостаза глюкозы\n\n"
          "Для отображения графика необходимо задать начальные условия модели\n"
          "пункты 1 или 2 в меню\n"
          "После вывода графика закойте выведенное онкно, для возвращения в меню\n"
          "Для выхода из программы необходимо выбрать 3 пункт меню\n")

    while True:
        i = input("Меню:\n1) задать базовые начения глюкозы и инсулина\n"
                  "2) использовать средние значения глюкозы и инсулина\n3) выход\n")
        if i == '1':
            Gb = (input("Вевдите базовое значение глюкозы от 3.9 до 7.1: "))
            while True:
                try:
                    Gb = float(Gb)
                    if (Gb >= 3.9) and (Gb <= 7.1):
                        # main()
                        break
                    else:
                        Gb = input("Введено некорректное значение\nВевдите базовое значение глюкозы от 3.9 до 7.1: ")
                except:
                    Gb = input("Некорректное значение\nВевдите базовое значение глюкозы (число) от 3.9 до 7.1: ")

            Ib = input("Вевдите базовое значение инсулина от 3 до 20: ")
            while True:
                try:
                    Ib = float(Ib)
                    if (Ib >= 3) and (Gb <= 20):
                        main()
                        break
                    else:
                        Ib = input("Некорректное значение\nВевдите базовое значение глюкозы от 3.9 до 7.1: ")
                except:
                    Ib = input("Некорректное значение\nВевдите базовое значение инсулина (число) от 3 до 20: ")
        elif i == '2':
            Gb = 5.5
            Ib = 15
            main()
        elif i == '3':
            break
        else: print("Такого пункта меню нет")

menu()