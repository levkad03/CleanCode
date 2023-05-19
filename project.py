import numpy as np
import matplotlib.pyplot as plt

DIAGNOZE = "Ймовірність діагноза %s = "

MULTIPLIER = 0.3333
POINT_1 = 1
AGE_20 = 20
AGE_40 = 40
AGE_60 = 60


def check_age(Age, sympthoms):
    age_ranges = {
        20: 1,
        40: 2,
        60: 3
    }
    for range_start, index in age_ranges.items():
        if Age < range_start:
            sympthoms[1, index] += POINT_1
            break
    else:
        sympthoms[1, 4] += POINT_1

    return sympthoms


def check_vomit(data, sympthoms):
    vomit_dict = {
        'yes': 1,
        'no': 2
    }

    sympthoms[2, vomit_dict[data[1]]] += POINT_1

    return sympthoms


def check_yellowness(data, sympthoms):
    yellowness_dict = {
        'eye': 1,
        'skin': 2,
        'no': 3
    }

    sympthoms[3, yellowness_dict[data[2]]] += POINT_1

    return sympthoms


def check_pain(data, sympthoms):
    # напади болю
    pain_dict = {
        'yes': 1,
        'no': 2
    }
    sympthoms[4, pain_dict[data[3]]] += POINT_1
    return sympthoms


def check_liver(data, sympthoms):
    # збільшення печінка
    liver_dict = {
        'yes': 1,
        'no': 2
    }
    sympthoms[5, liver_dict[data[4]]] += POINT_1
    return sympthoms


def check_appetite(data, sympthoms):
    # апетит
    appetite_dict = {
        'yes\n': 1,
        'no\n': 2
    }
    sympthoms[6, appetite_dict[data[5]]] += POINT_1
    return sympthoms


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

    Sympthoms = check_age(Age, Sympthoms)
    Sympthoms = check_vomit(data, Sympthoms)
    Sympthoms = check_yellowness(data, Sympthoms)
    Sympthoms = check_pain(data, Sympthoms)
    Sympthoms = check_liver(data, Sympthoms)
    Sympthoms = check_appetite(data, Sympthoms)

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

    Sympthoms2 = check_age(Age, Sympthoms2)
    Sympthoms2 = check_vomit(data2, Sympthoms2)
    Sympthoms2 = check_yellowness(data2, Sympthoms2)
    Sympthoms2 = check_pain(data2, Sympthoms2)
    Sympthoms2 = check_liver(data2, Sympthoms2)
    Sympthoms2 = check_appetite(data2, Sympthoms2)

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

    Sympthoms3 = check_age(Age, Sympthoms3)
    Sympthoms3 = check_vomit(data3, Sympthoms3)
    Sympthoms3 = check_yellowness(data3, Sympthoms3)
    Sympthoms3 = check_pain(data3, Sympthoms3)
    Sympthoms3 = check_liver(data3, Sympthoms3)
    Sympthoms3 = check_appetite(data3, Sympthoms3)

PrK3 = Sympthoms3 / Diagnose3
print(PrK3)

# В этих трех строках происходит вычисление числителя для каждого из трех диагнозов. Каждая строка представляет
# собой произведение вероятностей различных симптомов, связанных с соответствующим диагнозом. Значение 0.3333
# представляет собой нормализационный коэффициент, который используется для приведения значений вероятности к диапазону
# от 0 до 1.
PrK_D1 = PrK[1, 3] * PrK[2, 1] * PrK[3, 2] * PrK[4, 1] * PrK[5, 1] * PrK[6, 2] * MULTIPLIER  # числитель
PrK_D2 = PrK2[1, 3] * PrK2[2, 1] * PrK2[3, 2] * PrK2[4, 1] * PrK2[5, 1] * PrK2[6, 2] * MULTIPLIER  # числитель
PrK_D3 = PrK3[1, 3] * PrK3[2, 1] * PrK3[3, 2] * PrK3[4, 1] * PrK3[5, 1] * PrK3[6, 2] * MULTIPLIER  # числитель

PrD1_K = PrK_D1 / (PrK_D1 + PrK_D2 + PrK_D3)
print("\n")
print(DIAGNOZE % 1, round(PrD1_K * 100, 2), '%')

PrD2_K = PrK_D2 / (PrK_D1 + PrK_D2 + PrK_D3)
print(DIAGNOZE % 2, round(PrD2_K * 100, 2), '%')

PrD3_K = PrK_D3 / (PrK_D1 + PrK_D2 + PrK_D3)
print(DIAGNOZE % 3, round(PrD3_K * 100, 2), '%')

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
