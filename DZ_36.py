def print_operation_table(operation, num_rows=6, num_columns=6):
    print('1 2 3 4 5 6')
    for i in range(2,7):
        line = [i]
        for j in range(2,7):
            line.append(operation(i,j))
        print(*line)

print_operation_table(lambda x, y: x * y)