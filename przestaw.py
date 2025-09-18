def przestaw2(n):
    liczba = 0
    n_str = str(n)
    n_list = list(n_str)
    for i in range(len(n_list)):
        for j in range(0, len(n_list) - i - 1):
            if n_list[j] > n_list[j + 1]:
                n_list[j], n_list[j + 1] = n_list[j + 1], n_list[j]
                liczba += 1
                
                
    final = ''
    for i in range(len(n_list)):
        final += n_list[i]  
    return int(final), liczba



n = input()
print(przestaw2(n))