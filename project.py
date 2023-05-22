import numpy as np
import matplotlib.pyplot as plt

DIAGNOZE = "Ймовірність діагноза %s = "

MULTIPLIER = 0.3333
POINT_1 = 1
INDICES = [3, 1, 2, 1, 1, 2]  # индексы для доступа к элементам массива

AGE_RANGES = {
    20: 1,
    40: 2,
    60: 3
}

VOMIT_DICT = {
    'yes': 1,
    'no': 2
}

YELLOWNESS_DICT = {
    'eye': 1,
    'skin': 2,
    'no': 3
}

PAIN_DICT = {
    'yes': 1,
    'no': 2
}

LIVER_DICT = {
    'yes': 1,
    'no': 2
}

APPETITE_DICT = {
    'yes\n': 1,
    'no\n': 2
}


def check_age(Age, symptoms):
    for range_start, index in AGE_RANGES.items():
        if Age < range_start:
            symptoms[1, index] += POINT_1
            break
    else:
        symptoms[1, 4] += POINT_1
    return symptoms


def check_vomit(data, symptoms):
    symptoms[2, VOMIT_DICT[data[1]]] += POINT_1
    return symptoms


def check_yellowness(data, symptoms):
    symptoms[3, YELLOWNESS_DICT[data[2]]] += POINT_1
    return symptoms


def check_pain(data, symptoms):
    symptoms[4, PAIN_DICT[data[3]]] += POINT_1
    return symptoms


def check_liver(data, symptoms):
    symptoms[5, LIVER_DICT[data[4]]] += POINT_1
    return symptoms


def check_appetite(data, symptoms):
    symptoms[6, APPETITE_DICT[data[5]]] += POINT_1
    return symptoms


def process_data(file_path):
    symptoms = np.zeros((7, 5))

    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    data_size = len(lines)
    diagnose_count = data_size - 1

    print("'диагноз' =", diagnose_count)

    for i in range(1, data_size):
        data = lines[i].split(';')
        Age = int(data[0])

        symptoms = check_age(Age, symptoms)
        symptoms = check_vomit(data, symptoms)
        symptoms = check_yellowness(data, symptoms)
        symptoms = check_pain(data, symptoms)
        symptoms = check_liver(data, symptoms)
        symptoms = check_appetite(data, symptoms)

    probabilities = symptoms / diagnose_count
    print(probabilities)

    return probabilities, diagnose_count


PrK, Diagnose = process_data("Stones_var5.csv")
PrK2, Diagnose2 = process_data("Ascariasis_var5.csv")
PrK3, Diagnose3 = process_data("Hepatitis_var5.csv")

# В этих трех строках происходит вычисление числителя для каждого из трех диагнозов. Каждая строка представляет
# собой произведение вероятностей различных симптомов, связанных с соответствующим диагнозом. Значение 0.3333
# представляет собой нормализационный коэффициент, который используется для приведения значений вероятности к диапазону
# от 0 до 1.

PrK_D1 = np.prod(PrK[range(1, 7), INDICES]) * MULTIPLIER  # числитель
PrK_D2 = np.prod(PrK2[range(1, 7), INDICES]) * MULTIPLIER  # числитель
PrK_D3 = np.prod(PrK3[range(1, 7), INDICES]) * MULTIPLIER  # числитель

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
