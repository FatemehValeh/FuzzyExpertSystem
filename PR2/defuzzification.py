import numpy as np


def integral(lower, upper, a, b):
    numerator = denominator = 0.0
    for x in np.arange(lower, upper + 0.0001, 0.0001):
        numerator += 0.001 * (x * (a * x + b))
        denominator += 0.001 * (a * x + b)
    return numerator, denominator


def health_defuzzy(y):
    a = -1.333
    b = 1.333

    if y == 1:
        numerator1, denominator1 = integral(0, 0.25, 0, 1)
        numerator2, denominator2 = integral(0.25, 1, a, b)
        return (numerator1 + numerator2), (denominator1 + denominator2)

    else:
        numerator1, denominator1 = integral(0, (y - b) / a, 0, y)
        numerator2, denominator2 = integral((y - b) / a, 1, a, b)
        return (numerator1 + numerator2), (denominator1 + denominator2)


def sick1_defuzzy(y):
    a1 = 1
    b1 = 0
    a2 = -1
    b2 = 2

    if y == 1:
        numerator1, denominator1 = integral(0, 1, a1, b1)
        numerator2, denominator2 = integral(1, 2, a2, b2)
        return (numerator1 + numerator2), (denominator1 + denominator2)

    else:
        numerator1, denominator1 = integral(0, (y - b1) / a1, a1, b1)
        numerator3, denominator3 = integral((y - b1) / a1, (y - b2) / a2, 0, y)
        numerator2, denominator2 = integral((y - b2) / a2, 2, a2, b2)
        return (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)


def sick2_defuzzy(y):
    a1 = 1
    b1 = -1
    a2 = -1
    b2 = 3

    if y == 1:
        numerator1, denominator1 = integral(1, 2, a1, b1)
        numerator2, denominator2 = integral(2, 3, a2, b2)
        return (numerator1 + numerator2), (denominator1 + denominator2)

    else:
        numerator1, denominator1 = integral(1, (y - b1) / a1, a1, b1)
        numerator3, denominator3 = integral((y - b1) / a1, (y - b2) / a2, 0, y)
        numerator2, denominator2 = integral((y - b2) / a2, 3, a2, b2)
        return (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)


def sick3_defuzzy(y):
    a1 = 1
    b1 = -2
    a2 = -1
    b2 = 4

    if y == 1:
        numerator1, denominator1 = integral(2, 3, a1, b1)
        numerator2, denominator2 = integral(3, 4, a2, b2)
        return (numerator1 + numerator2), (denominator1 + denominator2)

    else:
        numerator1, denominator1 = integral(2, (y - b1) / a1, a1, b1)
        numerator3, denominator3 = integral((y - b1) / a1, (y - b2) / a2, 0, y)
        numerator2, denominator2 = integral((y - b2) / a2, 4, a2, b2)
        return (numerator1 + numerator2 + numerator3), (denominator1 + denominator2 + denominator3)


def sick4_defuzzy(y):
    a = 1.333
    b = -4

    if y == 1:
        numerator1, denominator1 = integral(3, 3.75, a, b)
        numerator2, denominator2 = integral(3.75, 4, 0, 1)
        return (numerator1 + numerator2), (denominator1 + denominator2)

    else:
        numerator1, denominator1 = integral(3, (y - b) / a, a, b)
        numerator2, denominator2 = integral((y - b) / a, 4, 0, y)
        return (numerator1 + numerator2), (denominator1 + denominator2)


def defuzzification(fuzzy_values):
    numerator = 0
    denominator = 0

    if fuzzy_values['healthy'] > 0:
        result = health_defuzzy(fuzzy_values['healthy'])
        numerator += result[0]
        denominator += result[1]

    if fuzzy_values['sick1'] > 0:
        result = sick1_defuzzy(fuzzy_values['sick1'])
        numerator += result[0]
        denominator += result[1]

    if fuzzy_values['sick2'] > 0:
        result = sick2_defuzzy(fuzzy_values['sick2'])
        numerator += result[0]
        denominator += result[1]

    if fuzzy_values['sick3'] > 0:
        result = sick3_defuzzy(fuzzy_values['sick3'])
        numerator += result[0]
        denominator += result[1]

    if fuzzy_values['sick4'] > 0:
        result = sick4_defuzzy(fuzzy_values['sick4'])
        numerator += result[0]
        denominator += result[1]

    value = numerator / denominator

    fuzzy_sets = []
    status = ''

    if value < 1.78:
        fuzzy_sets.append('Healthy')
    if 1 <= value <= 2.51:
        fuzzy_sets.append('Sick1')
    if 1.78 <= value <= 3.25:
        fuzzy_sets.append('Sick2')
    if 1.5 <= value <= 4.5:
        fuzzy_sets.append('Sick3')
    if value > 3.25:
        fuzzy_sets.append('Sick4')

    # making return statement
    for item in fuzzy_sets:
        status += item
        status += ' & '

    status = status[:-2]
    status += ': ' + str(value)
    return status


