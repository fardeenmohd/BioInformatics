import numpy as np

BLANK = "-"


def score_function(a, b):
    if a == b:
        return 1
    if a != b:
        return -1
    if a == BLANK or b == BLANK:
        return -2


def initialise_matrix(seq_a, seq_b):
    seq_a = BLANK + seq_a
    seq_b = BLANK + seq_b

    matrix = np.ndarray(shape=(len(seq_a), len(seq_b)))

    for i in range(len(seq_a)):
        for j in range(len(seq_b)):
            if i == 0 and j == 0:
                matrix[0][0] = 0
            else:
                pass
