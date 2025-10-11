import math

n = 0
while True:
    n = int(input("Введите нечетный размер матрицы(нечетное число) минимальное число - 5 (если фигура - это сердце то 17): "))
    symb = input("Введите символ контура у фигуры: ")[0]
    figure = input("Введите фигуру"
                   "\nПримеры:"
                   "\n\tКвадрат (1)"
                   "\n\tТреугольник (2)"
                   "\n\tРомб (3)"
                   "\n\tКруг (4)"
                   "\n\tСнежинка (5)"
                   "\n\tСердце (6)"
                   "\n--- ")
    if ((figure.lower() != "6" and figure.lower() != "сердце") and n % 2 != 0 and n > 4) or ((figure.lower() == "6" or figure.lower() == "сердце") and n % 2 != 0 and n > 16):


        matrix = [[" " for i in range(n)] for j in range(n)]



        if figure.lower() == "снежинка" or figure == "5":
            for x in range(n):
                matrix[x][x] = symb
                matrix[x][n - x - 1] = symb
                matrix[x][n // 2] = symb
                matrix[n // 2][x] = symb
        elif figure.lower() == "квадрат" or figure.lower() == "1":
            for x in range(n):
                for y in range(n):
                    if x == 0 or x == (n - 1):
                        matrix[x][y] = symb
                    elif y == 0 or y == (n - 1):
                        matrix[x][y] = symb
        elif figure.lower() == "треугольник" or figure == "2":
            for x in range(n):
                for y in range(n):
                    if (x == n - 1 or y == x or y == n - x - 1) and x > n // 2 - 1:
                        matrix[x][y] = symb
        elif figure.lower() == "ромб" or figure == "3":
            for x in range(n):
                for y in range(n):
                    if (x == 0 or y == x or y == n - x - 1) and x > n // 2 - 1:
                        matrix[x - n // 2][y] = symb
                    if (y == x or y == n - x - 1) and x < n // 2 + 1:
                        matrix[x + n // 2][y] = symb
        elif figure.lower() == "круг" or figure == "4":
            for x in range(n):
                for y in range(n):
                    if x == 0 or x == (n - 1):
                        matrix[x][y] = symb
                    elif y == 0 or y == (n - 1):
                        matrix[x][y] = symb
                matrix[0][0] = " "
                matrix[0][n - 1] = " "
                matrix[n - 1][0] = " "
                matrix[n - 1][n - 1] = " "
        else:
            for x in range(n // 2):
                for y in range(n // 2):
                    if (x == 0 or y == x or y == n // 2 - x - 1) and x > n // 4 - 1:
                        matrix[x - n // 4][y + 1] = symb
            for x in range(n // 2):
                for y in range(n // 2):
                    if (x == 0 or y == x or y == n // 2 - x - 1) and x > n // 4 - 1:
                        matrix[x - n // 4][y + n // 2] = symb
            for x in range(n):
                for y in range(n):
                    if (y == x or y == n - x - 1) and x < n // 2 + 1:
                        matrix[x + n // 2 - 1][y] = symb
        row_counter = 0
        for row in matrix:
            element_counter = 0
            if figure.lower() == "сердце" or figure.lower() == "6":
                row_counter += 1
                if row_counter == n // 2 - 1:
                    for y in range(n):
                        if (y == 0 or y == n):
                            matrix[row_counter][y] = symb
                        else:
                            matrix[row_counter][1] = "И"
                            matrix[row_counter][2] = "в"
                            matrix[row_counter][3] = "а"
                            matrix[row_counter][4] = "н"
                            matrix[row_counter][5] = "_"
                            matrix[row_counter][6] = "Н"
                            matrix[row_counter][7] = "и"
                            matrix[row_counter][8] = "к"
                            matrix[row_counter][9] = "о"
                            matrix[row_counter][10] = "л"
                            matrix[row_counter][11] = "а"
                            matrix[row_counter][12] = "е"
                            matrix[row_counter][13] = "в"
                            matrix[row_counter][14] = "и"
                            matrix[row_counter][15] = "ч"
                for element in row:
                    element_counter += 1
                    Name = "Иван_Николаевич"
                    if Name.find(element) == -1:
                        print(element, end='  ')
                    else:
                        print(element, end='')
            else:
                for element in row:
                    print(element, end='  ')
            print()
    else:
        print("Попробуйте еще раз!")