number_of_test_cases = int(input())

for i in range(number_of_test_cases):
    number_of_days = int(input())
    solution_attempts_by_days = input()

    last_day_of_task = dict()
    not_suspicious = True

    for current_day, task_name in enumerate(solution_attempts_by_days):
        if task_name not in last_day_of_task:
            last_day_of_task[task_name] = current_day
        elif last_day_of_task[task_name] == current_day - 1:
            last_day_of_task[task_name] = current_day
        else:
            not_suspicious = False
            break

    if not_suspicious:
        print('YES')
    else:
        print('NO')
