def age_predicate(patient, psychologist, column):
    age = psychologist[column]

    for age in range(age - 5, age + 5):
        if patient.age == age:
            return 1

    return 0


def compare_predicate(patient, psychologist, column):
    if psychologist[column] == getattr(patient, column):
        return 1

    return 0


def checkbox_predicate(patient, psychologist, column):
    score = 0
    races = getattr(patient, column).split(" ")

    for race in races:
        if race in psychologist[column]:
            score += (1 / len(races))

    score += 0

    return score
