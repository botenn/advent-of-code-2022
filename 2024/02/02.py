import os


def is_safe(report):
    if len(report) != len(set(report)):
        return False
    ascending = report[0] < report[1]

    for i in range(len(report)):
        if i == len(report) - 1:
            break
        if ascending:
            diff = report[i + 1] - report[i]
        else:
            diff = report[i] - report[i + 1]
        if diff <= 0 or diff > 3:
            return False
    return True


def problem_dampener(report):
    for i in range(len(report)):
        partial_report = report[:i] + report[i + 1 :]
        result = is_safe(partial_report)
        if result:
            return True
    return False


with open(os.path.join(os.path.dirname(__file__), "02-input.txt")) as input_file:
    reports = [line.split(" ") for line in input_file.read().splitlines()]
    reports = [[int(item) for item in report] for report in reports]

safe_reports = 0
dampened_safe_reports = 0

for report in reports:
    if is_safe(report):
        safe_reports += 1
    if problem_dampener(report):
        dampened_safe_reports += 1

print(f"part 1: {safe_reports}")
print(f"part 2: {dampened_safe_reports}")
