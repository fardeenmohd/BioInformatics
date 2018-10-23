import numpy as np

BLANK = "-"
LEFT = "L"
RIGHT = "R"
DIAGONAL = "D"

def score_function(a, b):
    if a == b:
        return 1
    if a != b:
        return -1
    if a == BLANK or b == BLANK:
        return -2

def initialise_matrix(seq_a, seq_b, local=False):
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
                if local:
                    selected_max = max(left, right, diagonal, 0)
                else:
                    selected_max = max(left, right, diagonal)
                matrix[i][j] = selected_max
                temp_direction = None
                if selected_max == left:
                    temp_direction = LEFT
                elif selected_max == right:
                    temp_direction = RIGHT
                elif selected_max == diagonal:
                    temp_direction = DIAGONAL
                elif selected_max == 0:
                    temp_direction = None

                direction_matrix[i][j] = temp_direction

    return matrix, direction_matrix

def find_similarity(seq_a, seq_b, matrix, direction_matrix):
    current_index = (len(seq_a), len(seq_b))
    current_direction = direction_matrix[current_index[0]][current_index[1]]
    res_a = ""
    res_b = ""

    while (current_direction != None) and (current_index[0] > 0) and (current_index[1] > 0) :
        if current_direction == LEFT:
            res_a = BLANK + res_a
            res_b = seq_b[current_index[1]] + res_b
            current_index = (current_index[0], current_index[1] - 1) 
        elif current_direction == RIGHT:
            res_b = seq_a[current_index[0]] + res_b
            res_a = BLANK + res_a
            current_index = (current_index[0] - 1, current_index[1])
        elif current_direction == DIAGONAL:
            res_a = seq_a[current_index[0] - 1] + res_a 
            res_b = seq_b[current_index[1] - 1] + res_b
            current_index = (current_index[0] - 1, current_index[1] - 1)

        current_direction = direction_matrix[current_index[0]][current_index[1]]

    return res_a, res_b 

def main():
    A = 'AGGTA'
    B = 'GAGTTCA'

    global_matrix, global_direction_matrix = initialise_matrix(A, B, local=False)
    global_result_a, global_result_b = find_similarity(A, B, global_matrix, global_direction_matrix)

    print("Sequence A was: "+ A + " after global alignment: " + global_result_a)
    print("Sequence B was: "+ B + " after global alignment: " + global_result_b)

    local_matrix, local_direction_matrix = initialise_matrix(A, B, local=True)
    local_result_a, local_result_b = find_similarity(A, B, local_matrix, local_direction_matrix)

    print("Sequence A was: "+ A + " after local alignment: " + local_result_a)
    print("Sequence B was: "+ B + " after local alignment: " + local_result_b)

main()
