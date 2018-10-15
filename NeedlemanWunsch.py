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

    matrix = np.zeros(shape=(len(seq_a), len(seq_b)), dtype=int)
    direction_matrix = np.empty(shape=(len(seq_a), len(seq_b)), dtype=str)

    for i in range(len(seq_a)):
        for j in range(len(seq_b)):
            if i == 0 and j == 0:
                matrix[0][0] = 0
                direction_matrix[0][0] = None
            else:
                diagonal = matrix[i - 1][j - 1] + score_function(seq_a[i], seq_b[j])
                left = matrix[i][j - 1] + score_function(BLANK, seq_b[j])
                right = matrix[i - 1][j] + score_function(seq_a[i], BLANK)
                selected_max = max(left, right, diagonal)
                matrix[i][j] = selected_max
                temp_direction = None
                if selected_max == left:
                    temp_direction = 'L'
                elif selected_max == right:
                    temp_direction = 'R'
                elif selected_max == diagonal:
                    temp_direction = 'D'

                direction_matrix[i][j] = temp_direction

    return matrix, direction_matrix


def main():
    A = 'ACCAGGTA'
    B = 'GAGTTCA'

    matrix, direction_matrix = initialise_matrix(A, B)


main()
