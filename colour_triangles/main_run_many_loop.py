from collections import defaultdict
from itertools import permutations

from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}
steps = None


def make_steps():
    global steps
    if steps == None:
        steps = {}
        for x in permutations('RRRRRGGGGGBBBBB', r=5):
            steps[x] = small_triangles(x)
    return steps


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def small_triangles(row):
    while len(row) > 1:
        row = ''.join([mix_colours(row[i][-1:], row[i + 1]) for i in range(len(row) - 1)])
    return row


class ValidationError(Exception):
    def __init__(self, message):
        super(ValidationError, self).__init__(message)


def do_row(row, i):
    global steps
    return steps[(row[i], row[i + 1], row[i + 2], row[i + 3], row[i + 4])]


def triangle(row):
    """
    Working too slow, actually slower than the original.
    Still processes the same number of items but the extra loops add to execution time
    :param row:
    :return:
    """
    if len(row) == 0:
        raise ValidationError("Row empty")
    if len(row) == 1:
        return row
    if len(row) < 8:
        return small_triangles(row)
    make_steps()
    while len(row) > 50:
        streams = defaultdict(list)
        j = 0
        streams[j] = list(row)
        for i in range(len(row) - 4):
            for j in range(10):
                step = j * 4
                if i >= step:
                    streams[j + 1].append(do_row(streams[j], i - step))
        row = streams[j]
    return small_triangles(row)


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
