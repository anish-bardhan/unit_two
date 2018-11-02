
matrix = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
for row in range(len(matrix)):
    total = 0
    count = 0
    print(matrix[col])
    for col in range(len(matrix)):
        total += matrix[col][row]
        count += 1
    avg = total/count
    print(avg)
