import random


def dice_rolls(num_rolls):
    sums = {i: 0 for i in range(2, 13)}  # Суми від 2 до 12

    for _ in range(num_rolls):
        cube1 = random.randint(1, 6)
        cube2 = random.randint(1, 6)
        total = cube1 + cube2
        sums[total] += 1

    probabilities = {total: (count / num_rolls) * 100 for total, count in sums.items()}

    return probabilities


def compare_probabilities(s_probs, t_probs):
    print("Порівняння ймовірностей (в %):")
    print(f"{'Сума':<5} {'Симуляція':<10} {'Аналітика':<10} {'Відхилення':<10}")
    for total in range(2, 13):
        simulated = s_probs[total]
        theoretical = t_probs[total]
        deviation = simulated - theoretical
        print(f"{total:<5} {simulated:<10.2f} {theoretical:<10.2f} {deviation:<10.2f}")


t_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}

num_rolls = 100000  # Кількість кидків
s_probabilities = dice_rolls(num_rolls)
compare_probabilities(s_probabilities, t_probabilities)
