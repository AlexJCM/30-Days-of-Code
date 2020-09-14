actual_date = list(map(int, input().split(' ')))
actual_day = actual_date[0]
actual_month = actual_date[1]
actual_year = actual_date[2]

expected_date = list(map(int, input().split(' ')))
expected_day = expected_date[0]
expected_month = expected_date[1]
expected_year = expected_date[2]

fine = 0

if (actual_year > expected_year):
    fine = 10000
elif (actual_year == expected_year):
    if (actual_month == expected_month):
        if (actual_day > expected_day):
            fine = 15 * (actual_day - expected_day)
    elif (actual_month > expected_month):
        fine = 500 * (actual_month - expected_month)

print(fine)
