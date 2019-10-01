def calculate_average(*args):
    sum = 0.0
    for arg in args:
        sum += arg
    return sum/3.0


assert 2.0 == calculate_average(1, 2, 3)
assert 3.0 == calculate_average(1, 2, 3, 6)
