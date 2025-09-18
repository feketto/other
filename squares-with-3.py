def squares_with_three(n):
    count = 0
    for i in range(1, n+1):
        square = i ** 2
        str_square = str(square)
        if '3' in str_square:
            count += 1
    print(count)
    return count

squares_with_three(10000)

