def flippingthematrix():
    m_len = len(matrix)
    n = int(m_len / 2)
    f_matrix = []
    for rows in matrix:
        if sum(rows[:n]) < sum(rows[n:]):
            rows = rows[::-1]
            f_matrix.append(rows)
        else:
            f_matrix.append(rows)
    # transpose the matrix
    # create an empty matrix the same size as the original matrix
    t_matrix = []
    for rows in range(len(matrix)):
        t_matrix.append([])
        for columns in range(len(matrix[0])):
            t_matrix[rows].append(0)
    # flip the rows again

    # transpose f_matrix into t_matrix
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            t_matrix[i][j] = f_matrix[j][i]
    final_flip = []
    for rows in t_matrix:
        if rows[:n] < rows[n:]:
            rows = rows[::-1]
            final_flip.append(rows)
        else:
            final_flip.append(rows)
    sum_n_n = 0
    # sum the top left quadrant of the matrix
    for i in range(n):
        for j in range(n):
            sum_n_n += final_flip[i][j]
    return sum_n_n


# flippingMatrix(matrix)