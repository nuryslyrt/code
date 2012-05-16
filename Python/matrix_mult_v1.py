#usr/bin/env python
#-*- coding: utf-8 -*-

print"UYARI !!!\n Bu carpım fonksiyonu sadece kare matrisler icindir.\n"

def make_matrix(rows, columns):
    matrix = []
    for row in range(rows):
        matrix += [[0] * columns]
    return matrix
    print matrix
    
def matriscarpmaca(a, b):
    #print"UYARI !!!\n Bu carpım fonksiyonu sadece kare matrisler icindir.\n"
    #a = input("Birinci matrisi giriniz : \n")
    #b = input("İkinci matrisi giriniz : \n")
    boyut = len(a)
    c = make_matrix(boyut, boyut)
    
    i = 0
    while i < boyut:
        i = i + 1
        j = 0
        while j < boyut:
            j = j +1
            k = 0
            while k < boyut:
                c[i][j] = c[i][j] + (a[i][k] * b[k][j])
                k = k + 1

    #for i in range(boyut):
        #for j in range(boyut):
            #for k in range(boyut):
                #c[i][j] = c[i][j] + (a[i][k] * b[k][j])

    print"\nSonuc matrisi = \n"

    for i in range(0, boyut):
        for j in range(0, boyut):
            print"%d  " %(c[i][j])
        print"\n"

matriscarpmaca([[1, 2], [1, 2]], [[1, 2], [1, 2]])
