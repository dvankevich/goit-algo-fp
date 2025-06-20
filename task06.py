# Данні про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


# Жадібний алгоритм
def greedy_algorithm(budget):
    ratios = {item: data["calories"] / data["cost"] for item, data in items.items()}
    sorted_items = sorted(ratios.items(), key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = []

    for item, _ in sorted_items:
        cost = items[item]["cost"]
        if cost <= budget:
            selected_items.append(item)
            total_calories += items[item]["calories"]
            budget -= cost

    return selected_items, total_calories


# Алгоритм динамічного програмування
def dynamic_programming(budget):
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.keys())

    for i in range(1, n + 1):
        item = item_list[i - 1]
        cost = items[item]["cost"]
        calories = items[item]["calories"]

        for b in range(budget + 1):
            if cost <= b:
                dp[i][b] = max(dp[i - 1][b], dp[i - 1][b - cost] + calories)
            else:
                dp[i][b] = dp[i - 1][b]

    selected_items = []
    total_calories = dp[n][budget]
    b = budget

    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(item_list[i - 1])
            b -= items[item_list[i - 1]]["cost"]

    return selected_items, total_calories


while True:
    try:
        budget = int(input("Введіть бюджет (або 0 для виходу): "))
        if budget == 0:
            break
        greedy_result = greedy_algorithm(budget)
        dp_result = dynamic_programming(budget)

        print("\nЖадібний алгоритм:")
        print("Вибрані страви:", greedy_result[0])
        print("Сумарна калорійність:", greedy_result[1])

        print("\nАлгоритм динамічного програмування:")
        print("Вибрані страви:", dp_result[0])
        print("Сумарна калорійність:", dp_result[1])

    except ValueError:
        print("Будь ласка, введіть дійсне число.")
