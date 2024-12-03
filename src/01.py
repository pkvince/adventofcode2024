from utils.api import get_input
from collections import Counter

input_str = get_input(1)
# input_str = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3"""


def a():
    lines = input_str.splitlines()
    left, right = zip(*(line.split() for line in lines))
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    sum = 0
    for i in range(len(sorted_left)):
        sum += abs(int(sorted_right[i]) - int(sorted_left[i]))

    return sum


def b():
    lines = input_str.splitlines()
    left, right = zip(*(line.split() for line in lines))
    left_set = set(left)
    right_occ = Counter(right)

    similarity = 0
    for val in left_set:
        similarity += int(val) * right_occ[val]

    return similarity


if __name__ == "__main__":
    print(a())
    print(b())
