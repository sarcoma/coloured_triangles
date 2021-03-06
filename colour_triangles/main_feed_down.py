from collections import defaultdict

from colour_triangles.bulk_test_benchmark import bulk_test_benchmark

RGB = {'R', 'G', 'B'}


def mix_colours(a, b):
    return b if a == b else next(iter(RGB ^ {a, b}))


def triangle(row):
    """
    Working too slow
    :param row:
    :return:
    """
    if len(row) == 1:
        return row
    if len(row) == 2:
        return mix_colours(row[0], row[1])
    streams = defaultdict(list)
    streams[0] = list(row)
    j = 0
    i = 1
    base = 0
    while len(streams[0]) > 1:
        for j in range(base, i):
            streams[j + 1].append(mix_colours(streams[j].pop(0), streams[j][0]))
        j += 1
        i += 1
    return streams[j][0]


if __name__ == '__main__':
    bulk_test_benchmark(triangle)
