from utils.api import get_input
import re

input_str = get_input(3)
# input_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
# input_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def sum_mul(input: str):
    matches = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", input)
    return sum([int(x) * int(y) for x, y in matches])


def sum_enabled_mul(input: str):
    segments = input.split("don't()")
    doable = [x.split("do()", 1)[1] if "do()" in x else "" for x in segments[1:]]
    rel_segments = [segments[0]] + doable
    return sum([sum_mul(segment) for segment in rel_segments])


if __name__ == "__main__":
    print(sum_mul(input_str))
    print(sum_enabled_mul(input_str))
