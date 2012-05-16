#usr/bin/env python
#-*- coding: utf-8 -*-

#ZİNNUR YEŞİLYURT ~~  ONDOKUZ MAYIS ÜNİVERSİTESİ ~~ SAMSUN

def make_matrix(rows, columns): #Sonuc matrisini sonradan güncellemek icin
                    #basta matris olusturudum.Bunun icin bu fonksiyonu yazdim.
    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]
    return matrix
    print matrix

def add_row(matrix):     #Matris boyularinin tekli sayi olmasi durumunda
                        #cifte cikarmak icin satir ve sutun eklemek icin  
    mrows = len(matrix)
    mcolumns = len(matrix[1])
    addr = make_matrix(mrows, mcolumns)
    matrix = matrix.append(addr)
    return matrix

def add_columns(matrix):   #sutun ekleme kismi.
    for row in matrix:
        row = row.append(0)
    return matrix

def matrix_divider(matrix):   #matrisi kendi icinde 4 parcaya bolen
                    #fonksiyon matrisi 4 parcaya bolup hesaplamak icin.
    tmp1 = []
    tmp2 = []
    tmp3 = []
    tmp4 = []

    i = 0
    for row in matrix:    #indislere gore parcalama kismi.
        for rowel in range((len(row)/2) + 1):
            if matrix[i] <= len(matrix):
                while 0 <= row[i] <= len(row)/2:
                    tmp1 = tmp1.append(rowel)
                while len(row)/2 < row[i] <= len(row):
                    tmp2 = tmp2.append(rowel)
            else:
                 while 0 <= row[i] <= len(row)/2:
                     tmp3 = tmp3.append(rowel)
                 while len(row)/2 < row[i] <= len(row):
                     tmp4 = tmp4.append(rowel)

def matrix_multiplier(matrix1, matrix2):  #matrix carpıcı

    if len(matrix1) % 2 != 0:  #matris boyutunun tekli sayi olma durumu icin
        matrix1 = add_row(matrix1)
        matrix1 = add_columns(matrix1)

        matrix2 = add_row(matrix2)
        matrix2 = add_columns(matrix2)
    #sonuc matrisini make_matris() metoduyla olusturma.
    result_matrix = make_matrix(len(matrix1), len(matrix1))

    while True: #while ile matrisi surekli kendi icinde bolup hesaplatma.
        matrix_divider(matrix1)
        matrix_divider(matrix2)
        matrix_divider(result_matrix)

        if len(matrix1.tmp1) > 1:
            while True:
                matrix_divider(matrix1)
                matrix_divider(matrix2)
                matrix_divider(result_matrix)
                if len(matrix1.tmp1) == 1:
                    result_matrix.tmp1 = (matrix1.tmp1 * matrix2.tmp1) + (matrix1.tmp2 * matrix2.tmp3)
                    result_matrix.tmp2 = (matrix1.tmp1 * matrix2.tmp2) + (matrix1.tmp2 * matrix2.tmp4)
                    result_matrix.tmp3 = (matrix1.tmp3 * matrix2.tmp1) + (matrix1.tmp4 * matrix2.tmp3)
                    result_matrix.tmp4 = (matrix1.tmp3 * matrix2.tmp2) + (matrix1.tmp4 * matrix2.tmp4)
                    break
        else:
            result_matrix.tmp1 = (matrix1.tmp1 * matrix2.tmp1) + (matrix1.tmp2 * matrix2.tmp3)
            result_matrix.tmp2 = (matrix1.tmp1 * matrix2.tmp2) + (matrix1.tmp2 * matrix2.tmp4)
            result_matrix.tmp3 = (matrix1.tmp3 * matrix2.tmp1) + (matrix1.tmp4 * matrix2.tmp3)
            result_matrix.tmp4 = (matrix1.tmp3 * matrix2.tmp2) + (matrix1.tmp4 * matrix2.tmp4)
            

    return result_matrix
    print result_matrix

#deneme 123 ses geliyor mu kaptan ???
    
matrix1 = [[1, 2], [1, 2]]
matrix2 = [[1, 2], [1, 2]]
matrix_multiplier(matrix1, matrix2)











