import numpy as np
import matplotlib.pyplot as plt

MULTIPLIER = 0.3333
POINT_1 = 1
AGE_20 = 20
AGE_40 = 40
AGE_60 = 60

Sympthoms = np.zeros((7, 5))
# -----------------D1---------------------
text_file = open("Stones_var5.csv", "r")
lin = text_file.readlines()
text_file.close()
D1Size = len(lin)
Diagnose = D1Size - 1


print("'камені жовчних проток' = ", Diagnose)

for i in range(1, D1Size):
    data = lin[i].split(';')
    # вік
    Age = int(data[0])

    if Age < AGE_20:
        Sympthoms[1, 1] += POINT_1
    elif (Age >= AGE_20) and (Age < AGE_40):
        Sympthoms[1, 2] += POINT_1
    elif (Age >= AGE_40) and (Age < AGE_60):
        Sympthoms[1, 3] += POINT_1
    else:
        Sympthoms[1, 4] += POINT_1

    # блювота
    if data[1] == 'yes':
        Sympthoms[2, 1] += POINT_1
    else:
        Sympthoms[2, 2] += POINT_1

    # жовтушність
    if data[2] == 'eye':
        Sympthoms[3, 1] += POINT_1
    elif data[2] == 'skin':
        Sympthoms[3, 2] += POINT_1
    else:
        Sympthoms[3, 3] += POINT_1

    # напади болю
    if data[3] == 'yes':
        Sympthoms[4, 1] += POINT_1
    else:
        Sympthoms[4, 2] += POINT_1

    # збільшення печінка
    if data[4] == 'yes':
        Sympthoms[5, 1] += POINT_1
    else:
        Sympthoms[5, 2] += POINT_1

    # апетит
    if data[5] == 'yes\n':
        Sympthoms[6, 1] += POINT_1
    else:
        Sympthoms[6, 2] += POINT_1


PrK = Sympthoms / Diagnose
print(PrK)


Sympthoms2 = np.zeros((7, 5))
text_file = open("Ascariasis_var5.csv", "r")
lin2 = text_file.readlines()
text_file.close()
D2Size = len(lin2)
Diagnose2 = D2Size - 1

print("\n")
print("'аскаридоз жовчних проток' = ", Diagnose2)

for i in range(1, D2Size):
    data2 = lin2[i].split(';')
    # вік
    Age = int(data2[0])

    if Age < AGE_20:
        Sympthoms2[1, 1] += POINT_1
    elif (Age >= AGE_20) and (Age < AGE_40):
        Sympthoms2[1, 2] += POINT_1
    elif (Age >= AGE_40) and (Age < AGE_60):
        Sympthoms2[1, 3] += POINT_1
    else:
        Sympthoms2[1, 4] += POINT_1

    # блювота
    if data2[1] == 'yes':
        Sympthoms2[2, 1] += POINT_1
    else:
        Sympthoms2[2, 2] += POINT_1

    # жовтушність
    if data2[2] == 'eye':
        Sympthoms2[3, 1] += POINT_1
    elif data2[2] == 'skin':
        Sympthoms2[3, 2] += POINT_1
    else:
        Sympthoms2[3, 3] += POINT_1

    # напади болю
    if data2[3] == 'yes':
        Sympthoms2[4, 1] += POINT_1
    else:
        Sympthoms2[4, 2] += POINT_1

    # збільшення печінка
    if data2[4] == 'yes':
        Sympthoms2[5, 1] += POINT_1
    else:
        Sympthoms2[5, 2] += POINT_1

    # апетит
    if data2[5] == 'yes\n':
        Sympthoms2[6, 1] += POINT_1
    else:
        Sympthoms2[6, 2] += POINT_1

PrK2 = Sympthoms2 / Diagnose2
print(PrK2)



Sympthoms3 = np.zeros((7, 5))
text_file = open("Hepatitis_var5.csv", "r")
lin3 = text_file.readlines()
text_file.close()
D3Size = len(lin3)
Diagnose3 = D3Size - 1

print("\n")
print("'паренхіматозний гепатит' = ", Diagnose3)

for i in range(1, D3Size):
    data3 = lin3[i].split(';')
    # вік
    Age = int(data3[0])

    if Age < AGE_20:
        Sympthoms3[1, 1] += POINT_1
    elif (Age >= AGE_20) and (Age < AGE_40):
        Sympthoms3[1, 2] += POINT_1
    elif (Age >= AGE_40) and (Age < AGE_60):
        Sympthoms3[1, 3] += POINT_1
    else:
        Sympthoms3[1, 4] += POINT_1

    # блювота
    if data3[1] == 'yes':
        Sympthoms3[2, 1] += POINT_1
    else:
        Sympthoms3[2, 2] += POINT_1

    # жовтушність
    if data3[2] == 'eye':
        Sympthoms3[3, 1] += POINT_1
    elif data3[2] == 'skin':
        Sympthoms3[3, 2] += POINT_1
    else:
        Sympthoms3[3, 3] += POINT_1

    # напади болю
    if data3[3] == 'yes':
        Sympthoms3[4, 1] += POINT_1
    else:
        Sympthoms3[4, 2] += POINT_1

    # збільшення печінка
    if data3[4] == 'yes':
        Sympthoms3[5, 1] += POINT_1
    else:
        Sympthoms3[5, 2] += POINT_1

    # апетит
    if data3[5] == 'yes\n':
        Sympthoms3[6, 1] += POINT_1
    else:
        Sympthoms3[6, 2] += POINT_1

PrK3 = Sympthoms3 / Diagnose3
print(PrK3)


# В этих трех строках происходит вычисление числителя для каждого из трех диагнозов. Каждая строка представляет
# собой произведение вероятностей различных симптомов, связанных с соответствующим диагнозом. Значение 0.3333
# представляет собой нормализационный коэффициент, который используется для приведения значений вероятности к диапазону
# от 0 до 1.
PrK_D1 = PrK[1, 3] * PrK[2, 1] * PrK[3, 2] * PrK[4, 1] * PrK[5, 1] * PrK[6, 2] * MULTIPLIER  # числитель
PrK_D2 = PrK2[1, 3] * PrK2[2, 1] * PrK2[3, 2] * PrK2[4, 1] * PrK2[5, 1] * PrK2[6, 2] * MULTIPLIER  # числитель
PrK_D3 = PrK3[1, 3] * PrK3[2, 1] * PrK3[3, 2] * PrK3[4, 1] * PrK3[5, 1] * PrK3[6, 2] * MULTIPLIER  # числитель

PrD1_K = PrK_D1 / (PrK_D1+PrK_D2+PrK_D3)
print("\n")
print("Ймовірність діагноза 1 = ", round(PrD1_K * 100, 2), '%')

PrD2_K = PrK_D2 / (PrK_D1+PrK_D2+PrK_D3)
print("Ймовірність діагноза 2 = ", round(PrD2_K * 100, 2), '%')

PrD3_K = PrK_D3 / (PrK_D1+PrK_D2+PrK_D3)
print("Ймовірність діагноза 3 = ", round(PrD3_K * 100, 2), '%')

X = [1, 2, 3]
Y = [round(PrD1_K * 100, 2), round(PrD2_K * 100, 2), round(PrD3_K * 100, 2)]
plt.bar(X, Y)
plt.text(X[0], Y[0], 'Камені', ha='center')
plt.text(X[0], Y[0] / 3, Y[0], ha='center')
plt.text(X[1], Y[1], 'Аскаридоз', ha='center')
plt.text(X[1], Y[1] / 3, Y[1], ha='center')
plt.text(X[2], Y[2], 'Гепатит', ha='center')
plt.text(X[2], Y[2] / 3, Y[2], ha='center')
plt.xlabel('Диагнозы')
plt.ylabel('Вероятность диагноза')
plt.show()
