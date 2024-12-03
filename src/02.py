from utils.api import get_input

input_str = get_input(2)
# input_str = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

reports = input_str.splitlines()


def is_safe(levels):
    # print(levels)
    direction = "up" if levels[1] > levels[0] else "down"
    for j in range(len(levels)):
        if j == len(levels) - 1:
            return True
        else:
            if direction == "up" and levels[j + 1] < levels[j]:
                return False
            if direction == "down" and levels[j + 1] > levels[j]:
                return False
            diff = abs(levels[j + 1] - levels[j])
            if diff < 1 or diff > 3:
                return False


def a():
    print("Part A:")
    safe_reports = 0
    for i in range(len(reports)):
        report = [int(level) for level in reports[i].split()]
        if is_safe(report):
            safe_reports += 1
    print(safe_reports)


def b():
    print("Part B:")
    safe_reports = 0
    for i in range(len(reports)):
        report = [int(level) for level in reports[i].split()]
        if is_safe(report):
            safe_reports += 1
        else:
            for i in range(len(report)):
                report2 = report[:i] + report[i + 1 :]
                if (is_safe(report2)) is True:
                    safe_reports += 1
                    break
    print(safe_reports)


if __name__ == "__main__":
    a()
    b()
