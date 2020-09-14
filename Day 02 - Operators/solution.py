# Complete the solve function below.


def solve(meal_cost, tip_percent, tax_percent):
    tip = (meal_cost * tip_percent) / 100
    tax = (meal_cost * tax_percent) / 100
    total_coast = meal_cost + tip + tax
    return total_coast


if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    total_coast = round(solve(meal_cost, tip_percent, tax_percent))
    print(total_coast)
