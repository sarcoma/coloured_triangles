from itertools import permutations

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


def triangle(row):
    """
    Working too slow
    :param row:
    :return:
    """
    if len(row) == 0:
        raise ValidationError("Row empty")
    if len(row) == 1:
        return row
    if len(row) < 8:
        return small_triangles(row)
    steps = make_steps()
    while len(row) > 8:
        row = [steps[(row[i], row[i + 1], row[i + 2], row[i + 3], row[i + 4])] for i in range(len(row) - 4)]
    return small_triangles(row)


if __name__ == '__main__':
    import time

    current_milli_time = lambda: int(round(time.time() * 1000))
    start = current_milli_time()
    assert 'G' == triangle(
        'BGGGBRGBBGBBRBRBRRBRGRRRRRBGBBGBBBGGBRGGBBRBGGGRRGGRBRRRBRBGGGBRGBGRGBGGBGGRBBRRRRRRRBRRBBGGRGGGGRRGGRBBGGGGRRGGGRRGRBGBGRRGGGGBRGRGBGRBRRBGBBGGGBBBRGBGRGBRGGGBRBRBBRGRGRGBGGGBBRBRBRBGRBRGGRGBRBBBGRRBBRBBGBBRGBRBRBGBRRBGGRRRRBGRRGGBGRBGBGRBRBRRBGRGBGGRRBBGBGBRRRBRRBGBBRGGBBBBBGBGRGGRBGBRBGGRRBBGGBRGBRBRRBBBBGBRGGGRBBBBBGRGBGBRBGGRRGGBBRBBRRGBBRBBBBRGRRBRBBRGRBRBRRBBBGRBRBRBGGRGBBGGRBGRBBGRBRBRGBBGGBRBRBRRBBBRGBRRGGGBBGGRBGRGBBGBRBRB')
    assert 'G' == triangle(
        'BRGGBGRBGRRRGGGBGGRBRBBRBRRRRGGGRBBBBGBBBBGRRGBRBRBBGRGBBGBGRBRBGBGBRGRBGGRRRBGRGBBBRBRRRRGGGBBRGRBBRBGRRRBGBBBRRGGBGGBRBBBBGRRRGGRGBRGRBRBGRBGGRRBBRGBGGBGGGGRRGBGGGRGBBGRRGBBRRBGGRRBGBRRBRRGRBRBBRGBGGBBGRBBGRRRBGRRBGGGGBGGRRRBRRBRRBBBBGBGRGBRBRBGBGRBGBBRGRRGRGBRRGGGRRGGBGBBGRGBBGGRBBGBBRGGBGBRGRGRRRBBBRGBGGRGBRRGGBBBRBGGGBBGBRBRGBBRBRRRRBGBGRGBRGBGRBGBBRBGBRBBBBBRGBRRRRGGRGBRBRGBBGBGGBRBRBRRBRGRGBRBBBBBBGGRGRGRRGRGGGGGBBGGGGGGBGBGBGBRBRGGBBBGGRRGGGGRBBRBRBGGBRBGGBGRRBRRRBBRRRRBGRBGRBRRBRRBRRBRBGBRBBBRGBGRBRBGRRRBBGBRGRBBRGBRGRRGRBBBGBGRBBBBGGGBGGBBBBRBGBBBBGBBGGBBRRBRGRBBGBBRRRBBRRRBBGRGGGBRGBBRGGRGGGGGBBGGRRGGBRRGRBGRBGBBRGBGBBGRRBBBGBRRRBGGBRGBGGGBRRBRGGRRGRGRRBGBRRGGGBBRBBRGBRGBGRGGRRGRRGGBRRGBBBBGGBGBRRBBRBGBBRRGGRGGGGBGBBGGGRGRGBBGBRGGBBGBBRRRBRRBBRGRBGRGBRGGRRBRRGRRGBGBBRBRGGRBRBGBBGGRRRGRGBBGRBRGBGBBRGBGBGRRBGGGRRGRGGGGGBGGGGRGRBBRGGRGBRGRRRRBRGBRGGRRRRGGBRRRRGGGBGGBGRRGRGRBGRBBGBGBRBBGBRBGBRBBBRRBGBGBRBRGGGGRGBGRGRGGBBRRGRRBRBBBGBGBGBBBRGRBBRRRRRRBBRBG')
    assert 'B' == triangle(
        'BBGRBRRRRBBRGBRRBGBRRBRBRBGGBBGBRRRRBGGGBGRGGGBBBRBBGRRRGBRGRGRBGRGRGBGBGGRRBRGGRBRGBRGGRRRGBRRBRGRRRGRBGBGGRRBBBGRBGGGGRBBGRGBBBBBGRRBBBGBRRRGBBRRBBGBGBGRRRBGGGGGBRBRBBBGGBGBGBBRGRGRRGBRBRRBGRGBBRGBGBGRBBBRBBGGRBGGRBBGBGRRRGBGRGBBRGGRGRRBRBGGRBRBRRBRBGRGBRGBGRBRRBRBRGRRGBBBGBRBBRGGRRBRGRRBBGGBBBRGBBGGBRGGRBRRGRRRBRGRGGGBBRGGRRBGGGBBGRBBGBBBBBRRRRBGBRGRRGGBBGBGBGBBB')
    assert 'B' == triangle(
        'GBBBBGBRBBGRRGGBBGRGRBGRBGBBBGGBBRGGGBGRRBBBRGGGGBRBRBBBBBRBBBBGGRRGRRBGRRRBBGGRGBRGGGBGGRGGBRBBRGRRGGBRBRRBGBBBGRRGBBRGGRRBGGRGBGBGGRBRRGGRGBBBGGRRBBBBBGRBGGRBBGBGGRRBGGBGGRRBRRGBGGGBGBRGBBBBRRRBRRRGRGGBRRBGRRBRBGRRRBBRRBBBGRGBBBRGBRBBRRGRGGRRGGBBGRGRGGBGBBRGBBGGBBBBGRGGRBGRGBRGGRRRGBGGRBBGGRBRRGRBRGRGBBRGBGRGBGBBRGRBGGBBBRBRRBBRBRRBGRGRRBBRBGGBGGGRGRRBGGBBRRBGBRRGRBBBGGGGRGBRGGBRBBGBBGBBBRGRRRRGBBRRGGBBGBGRGGBBGBRBGGRBBBRBRBGBBGBGGRRRRGBRGRBRBGBGGBRBBRGBBBRBGRRGRRBBRGRGBRRBGGBBRGRGBGGRRRBBRRRGBRBRRRBBBGBBGRBBRRBBRGRGBBRRBRGRGBBBRGRGBRRGGBBGGBRBGRGBRBBBRRBRGGGBGBRRBBGGGRBGGBBBBGBRRGRBGRRRBGGGGRBBBGBGGGGBRGRRRBBGGRRRBRBBRRRGRRRRBGRBGRRRBBGGRGGGBBGRBRBBGRRGRGGBGBBBBBRGBGGGBGBRBBRGGGBRRGBRRRGGRRRRBGGGBGRBGGBGRGGRRBGBRGRGRGBBBGRBRRRRGGRBGBRBRRBGBRBBRBGBGBRBGRRBRBGRBGGGGBRGBBBBGRBBGGGGRBRBBBRBBBRBBBBRBBBBGGRRBGGBGRGBBBGBGRRBBBBGRGBBGRRBGRBRBRBBRRGBBGBBRBGBRBBGRRRGGRGGGRGGRGGRBRRBRRGRRGGRGGGGGRGGRBGRBGBBRRRRGBGRGRGGGRGRRBBRGBGGGGGBBGRRBGGGGBRRBBRRBGGRGGGBGGBRRGBRBBGGGBRBBRRGBRRGRBGGGBGBGBGRGRGBRBRGGGRBGRGRGRBRBBRRBBGBRBBBBBRGRGRRBRRGGBBRGBGBRRGRRRRBGRBGRBBRRBGGRGRGRBRGRRGRGGBGBGBRGRRGBRBGBRRRBGBBBGRBBRGBRGBRBRBRGGRRRGBGBRGRBRBBRRRGBGRGRRGGBRBBBBBRGRGGGRRBGBRRBRBGRRRBBGGBGBGGGBBBGBRBRRRRRGBGRBGRBRRRRGBBBBRBBBRGRBRBRBBGGBGRBGRRRRBBRGBRGBGGBGGBRGBRGGRRBGBGRRRRBRGRRGRGBBRGRGGBBBRGGGRRRRBGGBBBRRRGBBRBBGGRGRBGRRGRGBRRGBBBGGRRGBRBGGGGRBGRBBBGBRRRRRBGRGGRRGRBBGBRGGGRBRGRGBBRGGRGRGBGRBGGBGBGRBGBRRBRBBBGGGRRRGBBRBGBRGBRBBBRBBGRBRGGGGGGGBRGBRGBRRRGBBRBBRRRRGBRRRBBBRGBRRRRGBBBBGRRBRBBRRRBRRRRGRRGRRRGGGRBRGGGBRGBBBRRGBRGRGRRRGGBGRRBRGRBBBGBRBGRBGRBBBGBBBRGGGGRRBRGGBGBRRRGBRBBRRRRGGRGRRRBGGGRBRRBGGBBBRBGBBRBBGRBGGGGGGGBGRRGBRRGRGRRRRGBRRRGBRBRRGRRGBGBGRGRGRRRRBRGBBBBBGBGGRRRGBGRRGBBGBGRRGRRGRGBGBGGBBGBGBBBBRRGRRBBRRGGRGGRGRGGGGGGGGRGBGBGGGBBGRRRRRRGRGBBBBGGRGRGRGRGBBRRBGGGRBBRRBGRBGGRBBBGRGGGGGBBBRRRBRRRRGBRRGGGBBBRRGBRGBGGBGRRRRRRRBRBRBRRGGBGGGBBGRBRGRGBBBRRBBRBGRBRBGRBRBGBBRBRBBRGBRRBRGGGGBGRRGGBGRGRGRRBGBBBGRRGBBBGRGRBRBBGGGBRGGRGGBGGGRBRGGGBBGRRGGRGRGRGBGBRRGRBBRBBBGRBRGGRGRBBBRGGBBRGRBBBBGGRRRGRBRGGRRBGGRRGBRBGRRBGBGBRGBBBRBBRBGRGGBGRBGGBRGGRGGBRGBGGBRGBBGGBBGBBGGBBGGRGBBGGRGBRGRBBBBGBBRBBGBBRBRGGGGRBGBRRRRRGRGBBRGGRRRBBRBRBBBBRBGRBBBBRRGGBGGRGRRBGBBRGBBRGGRRBGRRGGGRGBBRRGGRBGBRBBRRGBGBRGGBRBRRGGRRGBGBGRBRGBRGBRBBBRRGRBBRGBGRBGBGBBRRGGBRRBRGBGRRGBGRGRGGBBGBRGRRRGGRRBRRBRGRRGBBBRGBBGRRBGGBBGRGGRRGGGGGBGGRGBRGBRRGRBRGGBGBRBBRBBRRGBRRRBBRBRGBRGBBGGRBGRRRBBRBGRBBRRBBRRRGBRRBBGBGGBRBRGRRRGRBBRBBRRBGBGBBGRBRGRRRGBBGGBGBBRGBBRGRGBGGBGRGRBGGRBGGBRGBGBRGRBRRGGBBGGGBRRBBGRRRGBRGRRRGGBGRBGBRRGRRRRGRGGBGGGGGRGBBBBGGGGBRBBRBGRBRGBGBGGBRRBRGGGBRBBRBGGBRBRGRGGBRBRGBGBBGRBRRRBRGBRRRGRRGGGGGRBBGBRRRRBRGGRRRRGRBBBGRGBBBBGBGRGRRRBRGGBBGRGBGRRGBGBRBBGBRRBGGGBGGRRBRBRRBBBRRGBGGRRBBBRRRRGBRRGGGRGGBRBGRRRGRGBRRGBBBRBGGRRGGBBBGRBGRRBBBGRGRGGGBGRRGGRRGBBRBBBRBGGBRBGBRRBGGRBGGGGGBRGRRBRBRGGBBBBRRGGRGGRBBGGRGGGGBRRBBBGBGGBBRRBRGRRBRBRBBGRGBRRBBGGRGRRRRGRGGRBGGGRBBBGGGGBBGBRGBRRGRBRGGBGBGRGGGRGGGRRRGRBBGRRRBBBGBRRGBGRGGBBRRRGBBGGBRRBBRGGRGRRBBBRRBRRBBBBGGGBRBGRGRBGRBRRRBBBRBBGGGGGRRBRGBBBGRBRGRRRBGBBRRRRRGRGGGRBGRGRGGGRRBBRGRGBBBRBGGRBBBBBRBRRRRGGRGRGGRGBRRRGRGRRBBBBBGRRBRGRGGBGRBBGBGRRBGBBGGRRGRRGBBGGRRBBBRRGGBBGBGRBRGGBRGGRB')
    assert 'B' == triangle(
        'GRRBBBGRBGGGGBGRGGRBRRBRGBRRBGGBRGRGBBRBRRBGRBBGRBRRBBRRBGRBBGRBBBGBGBBBRRGRBBGGGRRRBGRGBGRBGRBRRBRGRRGGGGRRGBGRBBRBBRRBGGGRGRRRBBRBBBGBRBBRGBRGGBRBBGRRBBGRBRGRGRGGGGRBBGRGRGGRRBRRBGRRRRGRGRBGGBGGGBBGBRRBGGGBGGGBGBGGRBRBRRRBGRGRBBRBGRRBBRGGRGRGGBGGRRRBBRRRRBGGGRRRRRGBBRGGRBRBGGGGGGBBBRGBGBRRBBBGBGBRRBGGGGGRBRGGRRBBGRRGRBRGRGRBRGGBGBBGGGGBBGGGGBGRRGBRBGBGGBRGBGGGGBRBBGBBGRBBRBRGGRGRGBRRGGRBBGBGRRGGGGBRGGGRBGRRRGBBGRGGGBRGBRBBRRGBBRBGGGGGGRGRGBBBGRGBBBRRBBRRBGGRRGBRGGRGRGRRRRGGBBRGBBBBGRGGGGBBBBRBBGBBBRBRGGRBGRBRBRBGGRBRBGBBBGRGGGGGGBBBRBBRBGRBBBGRGBGBBRRGBGBBRRBBRRGRGBBBRRRBRBRBBGBGRGRRRGRRRBGGRGGGGRGBGRGGGGGRBGGBRRBBBGRRGRGBGGGBRRGBGRRBRGGGGBGBRRBBRBRRGGRRRBRRRRBGBGGBBGGBBRBRBGGBBBGBBGGRGGGBGRRBRGGRBGBBBBRBBGGGRRRGRRGGBGBBGRGBRGGGRGBGBGBRBBBBRRBBBRGBBGRRGGBRRGGBGRRRRBRGRBBBGGGBBGRBBRBBRBRGRBRBRRRRBBGRBRGBGBRGBRBGGGRGRBGRGGRGGBGGRBGRRGGRRGGRRBRRBBRGBBRBBBGBBGRGGBBRGGRGRRGBGGRGGRGBBBBBRGGBGRRRGRGBGGRGBBGRBBGRBRRRGGGGBGRGBBRBBGRRGRBGGBBRGRBBGBRRBRBGGBBRBRBRBRBRGGGRGGGGGBBGBBRRGBGRBGRRGRBGRGBRGRGRRRRRBBGRRRRBGBRBGRRGRRBBGRBGBGGRRBBBGRGGGGGRGRRBGGBRBGBBBGGGGGBGRGRBBGBBBGRRBBGGBGRRRRBRRRBBBBGRBGGRRBBGBRBGBBRGGBRGRRGRGRGGRRGBRBGRBBRRBGBBRBBBBRGBGBBGBBBBRRRBBBRBRGBBBGBBGGBGRGBGBBGRBGRBBRRRGRGBRRGBRGRBBRGGBBGRBGRRGRRBRGRGGBGRGRBRRGGGGRBBRBBGRRGRBGRRGGRBBBGBRBRRBBRGGGRBGGRGGGBGRRGGRGBGRBRBBRBGRGRGGRBRBBRBRGGGBBGBRGRGBGRGRBGGBGBBGGGBGRRRRGGGRGBBGBBBRGBBGGBGGRBBGBBRRRRGRBRBRRRRGRRRRGBRRBBRBBGRBBGRRGRRRBRGRBBRBRRGRGGBGRGRRGBRGBBGBGGBRRGBBGBGRRRRRGGRGGGGRBBRGRBRBRBGRRRRGGBBGGGGGGBRRBRBBRBRGBRGGRRBGBBBGRGRGGGBBRRBGGBBBGBBGRGGBBRBRRRGBGGRBRBRBRGBGRBBGGGGRRBBRGGGGGRGRGRGRBGGRBGBBGRGGBGBRRBGBBRBBBRGRGRGRRRBGBBGRBRRGGBGRRBGBGRRBRRRRBRGRBGGBGBBBRBBBBRRBGGRRGGBRGBGBBGRBRRGGGRBBGRGRBBBGGBRRRBGGRGRBRGBGRRGRRGRBGRGRGRRBBRGBBBBBRRGRGGGGBRGRRGRRGRBGGRGRRGBGRRRBBRRBGGGGBBGGRGGGGGRGBBBGRBBRBRBBRRBGBRGBGBBBGGBGBGBBGBGRBRGBGBBGGBRGBBRBBBGRGRBGGBGGBGRRBRGBBGRRGRRGRBRGRRBGRRRGRGBRBBGGBRRGBRRRRBRRGBBGBBRRBRRGBRBRBGRRGRGRBRGRBRBBGGRGRGRGRRGGBGGBRRRBGGRGBBRGGBBGGBBRBBRBBRRRGBGGRBRBGRRRRGRGBRRBGRBGBBBRGBBRRGRBGRGRBBRGRGGRGRRRBRBBGRBBGRRRGRGBBGGBGGBGRBGGBRBBGGBGBBBGGBBRBGBBGBGRGGRRRBRBBBBRBRBGBRRBBGRGBGRGBRGBGGBRRBBRBGGGBRGBBGBRGGGRBBRRRBGGRBBGRGBRBRBRBGBBBRGGGGBGBBRBRBGBGRRGBRBGRBBRGBRBRGRRGBGGBGBBGRBRBGGRGGGGRBBRGGRRRGRRRGBGRRBBBRRRRRRBBRGRGRBGBBBGRGBGRGRBGRGBBGGRGBRBGBGGBRGGGGGRGGGRBGBGRRRBBBBRGGGGBGGBGGRGRGRGBGGRRBRRBRGRGGBGBRBRGBGRRRRBRRGBBBBRBGBRGRRBGBRBRRGRGGRBRGRRBBBBBGGGBBRRBGBBRBGGBRGGGRBGBRBGBGRRBGGGGGRBRRRBGGBGBRBGBGBRRBRBBBGBBGBRBRGRRRRBBRRGBGBBRRBGRRGGBRGRGBRGRGGRBGRRGBGBGRGRRRBBGBRBGRBGRRRBGBGRBRRGBRGRBGRBGGBGRBBGBBBGBBRBBBBBBRBGRRRGBGGRGBRBGGBBRRGGGBBGRGRBRRGGRGBRBBRBRGBRRGBBGGRRBRRBBRRBBBBGGGBGBRGRGBBGGBGGBGBBGRGBBRGGGGGBGRRRGBGGGBBGRRBRBGBRRRGGGRRRBRBBBRRBBGRBBRRGGRGBBGGRBRRRBRBGBBGGGGBBRRGRGBRBRGBGGBBGBRBBRGBGRGGBGGRGGGGBBBGRBGGGRGRRBGBGRGRBRRBBBGGGRRBRBGRGBGGGBBGBGGRRBGRBRBRGRGGBBBGRGBRGRGRBGBBBBGRRGRBGGGBBGGRRGGGBRBBGGBBGRGRBGGGRRGGGGGGGRGRBBGGGBBRBRRRGRBBRGBRBBGGRBBBRBRBBGGBGGBRGGBRRRBBBRGGBBBGBGRGGRBBBGRRGBRGBGGRRBRBRBGGBRGRBGGRRRGRRRRBBGGRGBRRBBBGRBBRRRGBGGRGRBGRGRRGBRBBRRRGRBGBGGBGGBRGRBBGGRBGRBBGRRRGRBRGBBRBRRGBGRBRBRBGGRRBGRRBBRRGGRBBRRGRGRRGBRGRBRGRBBRGRGGBGRBRRBGGGRBRRGBBRGRGRRRGRGBGRGGRGBBGBBGRBBBGGGGGBGRBGGBRBGBBRGRRRRRGBRRGBRGBBGRRBBRRBGRBBRBBBGBGRRRRGBGRGGGRBBRBBGBBBBRGGBRRRBBGGBGGBGGGBRGGBGGGRGBRBRBRRGRRBBBGBBBRGGBRRGGGBBBGGRGRBRRRBRRGRBRBBBRRGGRGGRRRRBRBBGBBRGRBBBRRGBRBBGGGRBBBBGBBGRBBGBGRGGBRRRGRRBGRBBGGGRGGBRBRRGBBGBBBGGRBGGBGRGRRRGRRBRBBGGBBBRBGRRGBGRBBRGGGRRGBGGGBRRGBRRGBGBBBBBBBRBRBGBRGBGRBGGBGRGGBBGBRBRRGRGBBGGGBGGRRGGGGBGRBBGRBGRBRGBGGRBGBBBBBGGGRBBGBGRRGRBBBBBBRRRGRRGRGGBGGRBBBBRGRBRGRRGRBGBBGRGGBGBRGRGRGGRBGBRRGRGRGRBRRBRBBGGGBGBRRGRBRRBRGRBRRGBRRGRRRRRRGBRGGGGBRBGGRRBRBBRBGBRBBBRRRRGBBGRGBBGRRGRGRRGRRGBBGGRGRGBRGRGBRRRGBGRRRRRBBGRRGBRRGGRGGRRRRBBGBGRRRRBBGRGGRRGRRBRGGBRBBBGGBRRRBBBGRRBGGGBBRBBRGGRBBGBGRGRRBBRGGGRRRGRBRBGRGRRBBGBGBGRRBRBRBRRGRBRRBBRBGGBRGGRGGBBGBRRBGBGGGGGGBGGRRRRGRBGRRBGRBBRRBRBRRBRGBGGGBRBBGGRRGRBRBGRRGRGGRRBRGRRRRBBBGGBGGRBGBBGGRGGBBGRGRBRBRRRBRRRBRBBBGBBGBBRRRGRGGGRGBBRBBRGRBBGGBBGGGBBGRRGRRBRRGGGGRBRBRRBGRRBRBGRGRGGBRBRBGBRBBBBRRGGGRBBGRGBRBRGGRRBGGRGRRBGRGBBGRRRRRRRGRRGBBBBBBRRRRBGGGGGGRBGGGGBGBRGGBGBGBBGRBGBBRRRGBBGRRRRBBGGBBBGGRBBRGRGGRGGGBRBBGGRBRGRGGRRRBGGGRRGBBGRRGRGBRBRGRGGGRGBGGBGGGGRGRRBRBGGGBRGGGRRGRRRGBBGRGRRBRBBBGRRBBBRBGBRGBRRBGRRRRBBRRBGRRBGGRGGBGBBRRGGGRBGRBRBRGBBBBRBGRRBBBRRBBGGGGRGGBGRRRRRBGGBGBRRGGGGBBBBRBGRGGRGBRRBRGRRGGGGGGGBGBRRRRBBGRRGGBGBGRGGGGBBBBRBGGRBRRGGGGBRGBRBGBGBBGRBGBBRGGGGRRRBBGRRGBRBBBGRGGBGGBRBBRRBRRGRRBRBGRBRBBBGRGBGRBBRBBGRRBRGGBBRRBGGGRRGBBGGGBBBRGGBBRRRGBGBGBGRRGRBBRGBGRGRGBGBBGBRRGGRGGGGGGGBBBRGGBBGRBBBBRRRRGRRBGRBBGBRBGBBRBGBBRRBRGBBBGBRGGRRBGGBRRBRGGGGRRRBGGRRRGBRBGGBBBGGBGBRGBRRRRGBBGBRRGRBGGGRRRBBRGRGBRGBRGRBBRRRGBGBRGGRRBBGBRGGRBBBGGRGBGRBBGBBRGGGRGGRBBGBRBGBGGRBBGGBGRGGGRGRRGBRRRBBGRGGGBBGRGBBBRGBGGRGBGBBGRGBGGGGBGRBGBGRGGBGBBRRRBBRBRBGBBRRRRGRRBGRRGGRRBRBGBRGGGGBBGRBGGGRGRGRBRBGGBBGGRRRRRRBRBBGRRRBRBRGGRBRGGBGGRRRGGGBRRGGGBBGBBGBBGBBGBRBRRGRGRBGGGRRGRBGBRGBBRBBBRRGGRGGRBGRRBBRGBRBBRRGGGRBRBRRBGRGRBRGRGRBRBRBBRRGBRBGBRRRRRBGRGRRBGRBBRRGRRRGBGGRBGBBRGRBRBBRGRRGBGRRRBRBBRGGBGGBRRGGBGRGGGRGBGBBGGGBBGGBBGRRGBBBBBGGBGBBGGGBRBGBBRGBBGBRBGBRGGGBRGGGGGGGBGGGGRGRGGRGBRRRBBBGBBBRBBBBRGGRBGBRRGBRGBRBGBBRBGGBRBBGGGGBRRGGBBRRGRBBRRBGBGGBBGRGGRBBGBRBBRGGRGRGBBGGRRRGRGBGGGBBBRGGBRGBGGBGGRGBBBGGRBBGGGRBRRRRRRRBGBBGBGBGBGRRBGRRBGRGBBBGGBBBBBRBGBBGGRRGRGGGBRGRRBBBGGBBRGBBRBBGRRRRBBBBBGBBRGGBRRGGRGRBRRRBBRBBBBRGRRGRGBGRRGRBGGBBGRBRGGRRGGGBGBBBBGRBRBBRRGRRRBBGBGRRGRRBBRRGGGRRBBBBBRBGRBGBBBBBGRRRRRGRRGBGRGRRGRBGRGBBRBGGRBBRGBBRBRGGGBRBGBBBRRBGGGGRBGRRBGGBRRRRGGGBBBRGBBBBRBGBBBGGBBRRBBBRBGBBBGBRBRBGRBGGRBGBGRRGGGRRGBRGRRBRGRBBRBBRBGRRGRRGGBGRRRGRBRBRGRGRRRGGGBGBBBBRBGBRRRRGBRRGBBRBBRGGGBGGRGGGRBBGGRBRBRBBRBRGRGBBRGRRGBRGBRGGGBBRRGRRBRBGGGBGBGRGRRGGRBGBGRRRGGBRRRBRBGBBGRRRGGRBGRBGGBRBBRGGRBBGGRBRBGRRBRBRBBGRRBGRRRRBRBGBRBRGGBBBBBRBRGGGGBBBGGGBGBRBRBBRRRBBGBGGRBGGRGGBRBRRGGRGGBBGBBGGGRGGRRBBGRGGBBRGBRRGBGGRRRBGBBRGBRRBRBBBBRBBRBGGRGGRBGGRGRRRGRGRGBBGGRBRBRBBBBGRRGBRGBGGRGRBRGRGGBGRRGGBRBGRGBGGGGBBGGGRBRRBRRBRGGGBBRRBBBBBGGBRGBRBRGGRGBRRRBRRRBRGBRRGBGBGGGRBGGGBGGGBBRRGRRBBBBBRRBBBGBGRBRRBBGRBBGBGBBRRRBRRBBGGRBGGRBRGGRRRGGBGBBBRRBGGGRBBRGRBBBGGBGRRRRGRRRGBRRRRGGGRGRRRRGBGGBRGGGRBGGRRBGGGBRBGGRBRBRGBGRRRGRRRGBGRGGBGGGRGRBBRGRBGRBBRBRBGRRGGGBRRRRRRRGBRGGGGGGRGRBBBRGBGGRRRRGRRBRBGGGGRBRRBBRRBGGBRBGGRBRRRGRBGRBRRRRRBRGBGGGBBGBGGBGBRRRRBRBBRRBBGRBBGRBRRBGBBGGGRRGRRBRBRGRBBRRGRGBBRRBBRBRBBBGBGBGBRGRBRRGRGGGRGBRRRGRBRGBGBRGRBRBGBGGGRBBRGRBBRRGRRGBGBRGRBRGBRRGRRGRGGBRBRRGBBBRGBGRRRGBGBRGRGGBBRRRRBGGRGRRBBRBGBRGRRGRBRGBGGBBGRRGBBBGRBRRBRGGRRBRGRRGBGBGRBRGGBBBBBRRGBBRGRRBRRGBBRBBRGRBBRRGBBGRRGGBGGGGRBRGGRRBGRBGRGGRGBGRBRRRGRRGBGBGRGRRBGBGGBGRBBBGRBRGBRRBBGGRRGRRRRGGGBGGBBGRRGRBGRRBRGRGRBBGBRRGRBBBGBBGRBGBBBBGGBGBRRBBRRBGGGRBRGBGBRBRRGGRRRRBBGRRRBGRGRRBBBBRBGBBGBGRBBGGRBRRGGBGGGBGGGRBRBBBBRBRBBGGGRGGRBRRGBRRBBBRBRRGRRRRRBGRBGBGRRBGBGBGRBBGRBBBRRBRGBGRGRGGGGRGGBGBBBRRGBGGGBBGBGBRBRBGBBBGGBB')
    assert 'B' == triangle(
        'BBBRGBGRGRGBGBRBBBGBRRGRBGGBBGBBRRBBGGBBRRBRGBGGGBRBBBGRGBBGBBBGGGRRGGRRBGGBRGBBRGBGBBBBGBRGRGBGBGRRRGBBRRRGBGRRRRBBBGRGBBGBRBGGGRBRBGBGGRBBGBBGRGBGGBBGRBBGBBRGRRBGGBBRGBGBBGGRRBGGBGBRBBGRGRRRGBBRBRRRRBGGGRGBRRRRRBRGRBBBRBGGGGGRGRBBRGRGGRBGRGBRBBBGBGRBRGBRRRGRGBGBBGGRRRGBBRGRRGGRBGGRBGRBBBBRBRBGBRBRRGBGGGGRGGBGRRRGBRBRGRGRRGBRBGBRGRBRBRRRRGRGBGGBBBBGRRRRGGBGRRBGGBBGRBRGRGRGBGGRRBRRRGBRRBBBBBBGGBGGRGGBBBGBGBRBBBGGGBGBBGRRBRRBBBRGGRRBRRRRGBRGGGBRRGGGRRBRBRGBRRRGBBBBRRRBGBBGGBGBBRGGRGRRBBRRRRGRGGBBGGRBGBGBBRRBBGGBGGGGBGGRBGRRGBGBRGBRBBBBGRGBRRGBBGBRRRGRBGRRGRBGGRGBRRRGRRGGGRGGGBRRBBRGRRRBBBGBRBBGBGRBGRRGGRGGBBGRRGBGGRGGRRBGRBGGGBRRBRBGBRBRGGBGGBRGGGGGBGRGGBGGBGRBRRBRGRGRRGRBGBGGRRRRGGBGBRRRGBBRGGRBRRRRGGBBGGBGBRRBBRRGGBBRRBBRGBGRRGGBRBRBRRRRBRBRBRGRRRRBGBBGGGGGGGRGGRRRGRGRGBGGGRRRGRGRGRGGRGBRGRGBGGRBBGBBBBGBGBGGGRBGRGRBRGBRBRBRGBRBGBBRBGRBBRGBRGGGBGBBBBBGBGBGRGRBGRRBRRGRGGBRRBBGBRGGRRRBRBGGBGRBBBBRRGBGGGGBRRGRRGGBBBGBRRRGBGRGGRGGBGRBRRBBRBRRBBRRRGGGRGGRBGRBRGGBRRGGGRGGBBBRBBBGGRGRRRBGGBGRGBRBBBRBBGRRBBGBBRBRGRRGGGRGGGBBGRBRGBRGBRGGGRBGBBGRRGRGGGRGBRGGBBRGRRRRBRRGBRGBRBGGGBBGRBGBBGGBBRGRRGBRRRGBGBBRBBBBRGBRGGBGBGGRRGRBBGBGBBRRGRGGGBRRGGRBRRGRGBRBGGBBBGRBRGRGGBRGRBBRGBGBBBGGGBRRBGGRBBRRBGBRBBRBBGGBRGBRRRGRGBGBRGRBRGBRRGGRRBBBBBRRRGRGBBBRBBRBGGGGRGGBGBGGGGBGBRGGGBRGGRGGGBRRGBRRRBGRBGRRBRRGBRBGBGBBGRBRBRBGGGBGBRBRGRRGRGRRBRGRBGBRGGRBRGBBGGGGRBBGGBGRBRRBRRGGRRGRRRBGBRBGRRRGGRRGRRBBRBBGRRBBGBBRRRGGRRRRBBGBGBBRGGRBRBBBRBRBBGRGGRBRRBRBBBBBGRBRRRGGBRRBBGRRGGRRBBBGGGGGBBRGGGGBRRBGRGGGGRGGRGGRRBGBRBGRGRGGRGBRBRBGGRBBBRRGBBGBGGBBRBBGRGBBBBGBGRGBRBGBBRBBGGGBBRBRBGBRRRBRGBGRBGGRGGRRGRGRGRGGGRRGBBBGBGGBGBBRGRBRGBBBRBRBBBBBGGBGBGBBBRBGGBRGBBGRRRGGRBBBGRRRRBGRRRGGRBRBRGBBGRGGRBGGGRGGBGRBGGGGRGBRGBGGRGGBBBBGBGRRGRGBBRGGRBGRGRGGBGGRGBRBRBRBBRBGBGGBRGGGRBGBBGGRRRBRGBRGRRBBRGRGRRRBGGGRRGGBRRGBBGBBGBBRBRBBGRRRBRGRBGRBBGRGGRBGBGGBGBGGGRGRGRRBGBRRGGGRRRRRGGGBRRBBBGGRGRRGGBRGGGBRBGGBRGGRGGGRBRRGGGBBBGGRBGGRBBGBBGBGRGRGGBBGGRGBRRBGRRGGGGGRBGBBBGGRGBGBGBRRRGGRGBRBRRRBGRGGRGBRBRGRRGRGRRRRRRRRRGRGGBBGRGRBRGRGRRBBBRGRRRRGRBGGRBGBRGGGRBGBGBGRBRBGRRBGBRRRGGGRBRGBGBBBBGRGBBBRGBBRGBBGRRGRBBBBRRRBGGGBGBRGBRBBGBRBGGRRGGGGGBBRBBRBRGGRBGBRGGRBGGGRRBGGBGBBRRBBRGBBBBRBRBGGBGGBBRGRRRBRGBRBRBBGBRBRGGRRBGBBRBRGGGGGBRGGGGBBGBGBRGBGBRRRGRGGGRRBRRBBRRRBRBRBRGGGGRRGBRGGRGBRBGBBBBBGBRRBBBRBGGBRBBGBGGRRRRBRGRGRGGGBGGGRRRGBRBRGRRGGBGRRBBBGBGRGRRBRBBGBGBBBBGGGBBRRGRRBRBRRGRGRBGBRGBGRBGGBRGBGGRGRRBGRBRRRRGGRBBBGRBGGBRRGRGGRRGGGBBBRRBBRGBGGBGRBRGBBRGRRRRBGGGBRGGGGRGBGRBRRBGRRGBRRBGBGRRGBBGRBGRBBRBGBGRBRBBRBBGBRGGRRGGRGBGGBGRRRRGRBGBRBBRGRRGBRRGBGRBGRBRGRGGRGRRGBRBBGBRRGRBGBBBRRGBBBGRRRRRRGBGGGGGGGGBBRBGBRBBBBGRRRRRBBGGBRRBGRBGRRRGGBGBBBRGGBRGRGBGRGRGBGGRBRRBRRBGGBGGBRBRGGRRBRRGRBGGGRRBRRGBBBBGGGBBRGRGBBBBRBGGBRRBBBGGBRGBRBBRGRRBRRBRGBBRRGRBGBBGGGGGRRGGRBGGGRBRBBBBRGGBBBBGGRGRRGGGGGGGRGRBGBGRBBGGRBRBBRGRRGRRRRRBGBBBBRBBRRGGBRGRGRGGBBBBRRGBGRBBGRRBGBRGBBBBGBRRRGRGBGGBGBRGBBRRGGGRGGBRBGBRBGGBGRGBBGRBBRBRRBBGBGGGGRGBRBRBBGGBRGBGGRGRRGBBRRBRRBRGRGGGGGRRGBBBGBBRGGRBGBGRGGGGGBGBBRRBRRGGRGGRGBRBRGRGGGRRBRBRGRRRGGBBGRRRRGBGGRRRBRRGGGRGRRBBGRBRRRGRRRGRGRGRGBBGBRGBGBBRGBRRRBGBGRRRRRBRBBGBGBRBBGBRGRBGBRRBRRGRRGBBBRRGBBGRBRBGBRRRBRBGBBGBGBBRRBRBBGRG')
    assert 'G' == triangle(
        'BRBGBRRRBBRGGGRBBGGGGBGBBRBGBGBGRGGRRRGBRBBRGBGRRRRGRRRRGBBRBBRGRBRRBGGGBGGRRRGRGGBGRBRBRRGRGBBRBBGRBGBRBGBRGGBBGGGGRBRRBBBBBRBBGBRBBBGBBBGRRRBBRBBRBGBGBRBGBGGBGGRBRRRRBBBBBGBGRGBGGBBBRBGRRRBGGGRRBRGBGRBBGRRRRBGGRGGRRRRBRRRBBBGBGBBBBBBGBBBRBGGRRBGBBGGRBBRRBGRBRBGGGGGRBGBGRGBGBRBGBRBRRRRRBBBRGBRBBGBRRRRRRBRBRRRGBRRBRBGBBGBGRGRGGBBBRGRBRGBGGGGBRBBBRBRBBRBBGGBRGGGGGRGGBGBGRRGBRBRRBBGGRRRGGBBRBBGGRRRBGRRBGGGRRGBBGRRBRGBRGGBRBBGRRBRGGBRGBRRGRGRGRBBRGGGGBRBBBRBBRGRGBGBRBBRRGGRGGBBGBRBBBGBBGBBBBGGGGGGBBRBBBRBGBBBBRBGGBRGGRRRRBGRGGRGRBRBRBRRGBGGRGGGGGRRGRBGGGGBGGBBBRBRRGRRRRGRRRBBGRGBBBBBGRBRBGGGGBGBBBRGGRGGRRBBRBBBRRGGBRBRGGGBRGBRRBGRBRBGBBRBBGRGRBGGBGGBRGBBGRGBGRGGBGBBBGGGRRBRBGRRBGGGBBGGRBBBRBBGBGGGRGGRRBGGBBRGGRGRRBRRRBBRRRRRGRBGRGRRRGBGGBRBBBRGRBRGGGGBRRGGBGBRGRGBRGGRRBGBBRBGRGRRRBBBBRGGBGGGRBBGBBGBGRBGRBBGGRRGBBGGGGBGGBRRGRGBBBBBRBBRGGGGRRGGBBGRBRRRGBBRBBBRBGGBGGGGRGBBGBBBGGRGBGBRRGGRBRBRBBBGRBRBGRRRGBGBGRGBBGBRRBBRRBRGRRRBGGGRBRRBRBGBRRBBGBRBRBRBBGGBGGGBBBGBGGGGBBRGBRBBBGBRRGRRBRGGGBBGRBGBRBRRGGGBRBRRBRRGGGGGGBBGGGBRRBRRRGGGBRBRRBRGBRBRBRRBBBGGBGGRRRGRBGBRBBGBGRBGBRBGBGBGGRBBRGRGGBGRRGRBBBRRBGGRBRBBGGGRGGBGGBGGBRBGGGGGGBGBBBGRBRBGBRRRGGBRGRRGBBGBGGGGGRGBGBRGBRBRGRGRRBBBRGRGGBBGBGGBGRRBGGGRGRRRRGBGGRRBRBBRRBGGBRRBRGBGGBBRRBBRBRBRBRRGBBGGBBRGRGRRGBRRBRBRRBBGGBBGBGRRGRGRRGRBRGRGBBBGGBRRRRGRRBBBBBBRRGRBBRRRBBGGBBRRGRBGRGBGGGGRRRRBRGBBRRGGBRRGGGBGGRGRGGRBGRBGBRBRBGRGGRGBBBRBRRRRBBRRBRRGGRBRGRBBBBRRBBRGRRGRBGRBBRBBGGRBGGBRRRBGGBRGBBBGGRGBRRBBGRRRRGBBGGBBRGRBBRRBGRRBRBBRGRGGRRGRBBGRGRRRBGRGBBRRBGRRBBRGBGGRGRBRRBGGBBBGGRRRBBRRRGRGRRBRBBRRRGGRRGRBGGGBBBRGRBBGGBGGBGGBGGRBBGBBRGRBGGRRBRBGGBGRBBBRBGGGBGGRRBRGBRBRGGGGRRGBRGGRGGRRBBGBBRBGGGGGBRBGGBGGBRBGGGGRRGRRRRRGGGBRGBRBRGBGGRBRRBRBBGRRGBGRRRGRBBGGBBRRRRBBRBGRBBGBRRBGGGGBRGRGGBRGGBBRRBBRBBGGBRBRRRRRRBGBBGRGBGRGBRGRBBRRGBBBRGRBGBGBGRGBRRRGBGGGGGRRGRBBGBGBBRRRGGGBBBBGBGBRBBBBBGGRBRGRBRBBGRGGRRGBRBGGRGGRRBRRGGBRBRGGRRBBBRBGBGRRGBBGRRGRBGBRRGGBRRGGRBRGBGGGRGGBRGBRRGBGRGRBBBBGGBRRGGRGGGRGBBBGGGGRRBGBGRBGRRBRBGRGGBGGBRBRBGGBRGRRBBGRGGBRRGGGGRRGBRBBGBRRRRRBBRGGRGGGBBRGBBGRGGRGBGGRRGBGRRBGRBGGRRBRGRRGBRBRBBGBRBGGBRGRGBBRBRGRGRRGGGGGBRBBGGBBGGBRRGRGRBBRGRBGRRGGBRBBBBRRRGGRGBRBRBRBBRBGBRGGBBBRGRRRGGBBGGBGRRRGBBRGGBGRBGBRBGGGGRGGGBGGRRGBR')
    assert 'R' == triangle(
        'RRBRBGRGGRRRBBGBBBRRBBBGGRGRRRGRGRBGGBBRRBBGRBBGRRBRRBRBGBBGRGGRRGRBBGRBRRBGBGRBGBRRBGBBGGRRBBGRRRRRRGGGBGGGRBGRRBBBBRGGBGRBGRBRRRRRGGGBGRGRRGBRBBBBGBRRGRGGGBBRRGRGGRGRRBRRGRGRBBBBBBGGGRGBRRBBBRBRGGBRGGRRGBRGBBRBGRBRBBRRGBGBGRBGGRGGBRGGRBGRGGRGGBRBRRRBRGGRBGRGRRGBGBBRRBBBBRGGBBBGRRRRGRGRBBBBRBBBGRBGRBRGGBRBBGBGGRGGGBGRRRRGRBBGGGBGRBBBGBGGRRBRGBBBBBGRBGGRBRGGBBGBRRBGRGRBBBRRRBGGBBBRRRRRRRRRBRRGGRGBGBRBGRRBRRBGGGGRRBRRBGRGRBBRGBGGRGGGGRRRGGRBBRGBGRRGGGBBBRRRGBGGGRGRBRRGGGRRBGRBRGRGRRRGBRGGBBRBRGRBRRBGBBGRRBGGGRBGBBBBRRRBRBGBRGRGBBGBGGGBGBBBRRBGGGGBBGRBRRGRBRBRGGRBBBGRBBBGRGGBGBGBGGBGGGGGGBRRGGRRRGGGBRRBGBBBRGBBGGBBGGRBBGBGGGRGRBGGGRRBBBBRGRGRGRBBRGBBGBRGRRGBRRRBBGRBGGGGBBGGGBGBRRBBGBGRRGGGBRRRGGGRGRGRGBBBRBGRBGGGGRGRGRGBGRBGBBGRRRBGGBGBBBGGBBRGBBRBGGRRBGBGBRGBGGGGGGRGRRBRBBBBGGRBBRBRBRRBBBGRGRGGGRBBGRRRGBBGRGGBRBRRBRRRBRGBGRGGBGGGRRGBBRRGBGBBGRBBBGBGBRGGRGBRBGRBGGRRGBBRBBRBGRRBGRRGGRRRBRRBGRRRRBRRGGRRBBGRBGBRRGBBBGGRGGRBBBGBGGBGGGRRGBGBBBBBRBGBGRBGBGBRGBGRBGBGRRRGRGRRBBGGBRRRRRRGBBRRBGRRRBGBBBRRBRRBRRRBBGGRGBGBGGBBRRBRBGBRRRGRGGBGGRGGBBGGRGBRRGRRGGRGBBRGGBBRRRGBBBGBBRRBRRGRGRGRGGBGGGGRBBBRBBBGBGRGBRGGGRGRBBGRGRGRGRBRGGRRRGBGGRBRGGBGGBBRGBGBRRRGBBGRRGRRGBGGGRRGRGBBRBBRRRRBGRGRGGBGRBGRGRGBGBBRGBGBBBBBGGGRBBBRRRBRGBRBRGRBRBGRGRRGGBBGGRBBRBGRBBRRBRBGRBRBGBRGRBGRRBBBRBGBRBBGRRBRRRRRGGBBBRGBGBRGGGBRGBRGBRBGBBGRBRBGRGRGRBGGRGRBGRBBRBGGRRRGRBGBBBBRGRBRRGGGBGBGBGBBRGGGGRRGBRRBBGGBRRGGGBBGGBBGRBBBGGBGGGRGBGBRRRBGGGGGRBGRGGBRBGBRGBGRRBBBGRGRBRBGRRGBGRGGBRGRRGBBRBBBBRGRGGRGRGRRBBRRRGRBGBGGGRGBGGRRRRBGRRBGGRBRGGRRGBGRRBBBBGGGGGGRBGRBBBBGBGRRGBGBBBGRRRBGRRGGRGBBBBGRBBBBGGRBBBBBBGBGRGBGRGRBRGGGBRBRBGBBRGGGBGRRRBBRRRRBRBGBRGGGBRRGBGBRRRRRGBGGGRGGBRGRRRBGRGRGBRGGGRGBBBBRRGBGBGGGBBBBGBGRBRRRGGGGRRRBGRBGBBGBBRGRRRRRGBBRBRRRBRBBRRGBGGBRGGBRBBBGBGRRGBGRRRBGBGBGGBRRBRGBGBRRBRGBRRBGGGRGBRGRRRBRBGBGBRBGGGGBRBGGGBGRGRGR')
    result = triangle('RBRGBRBGGRRRBGBBBGGRBRGBRBGGRRRBGBBBGG')
    assert result == 'G'
    print(current_milli_time() - start)
