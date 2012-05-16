#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Denklem sistemlerinde gauss indirgemesi yapmasi icin tasarlanmistir.
#ZİNNUR YEŞİLYURT

class Matrix:               #Denklemi ifade etmem için gerekli olan matris sınıfı.
    def __init__(self,m,n,data=None):
        self.m = m
        self.n = n
        self.data = data or [[0]*n]*m
 
    def get(self,i,j):          #Matrisin i.satir j.sutundaki elemanini donduren fonksiyon.
        return self.data[i][j]
 
    def set(self,i,j,v):
        self.data[i][j] = v
 
    def swap_row(self,i,j):     #dizide eleman takas etmek için fonksiyon.
        """swap row i and j"""
        self.data[i],self.data[j] = self.data[j],self.data[i]
 
    def map_row(self,func,i):       #dizi elemanlarini toparlamak için.
        """evaluate `func` on the row i"""
        self.data[i] = map(func,enumerate(self.data[i]))
 
    def show(self,label=''):     #ismiyle ayni, gösterme fonksiyonu,bir nevi __repr__ gibi.
        if label:
            print label
        for l in self.data:
            for x in l:
                print '%6.3f' % x,
            print
 
class Solver:                              #Matris olarak alinan denklemin çözümü icin gereken fonksiyonlari cozum sinifi altinda topladim.
    def solve(self):   #asil cozme fonk gauss sinifinda yapacagiz ;)
        pass
 
    def find_pivot(self,i,j):                                           #Denklemde gauss indirgemesi icin pivot deger gerekir. 
        """find pivot in column j, starting in row i"""
        max_val = self.get(i,j)  #matrisden i,j den eleman alinmasi.    #Ucgen matris haline getirilirken birinci degisken sifir yapilirken mesela a11 pivottur.
        max_ind = i                                                     #2.satirda sifir yapilirken a22 pivottur gibi.
        for k in range(i+1,self.m):      #matris icinde dolasma.        #Bu fonksiyonda matrisdeki gauss işleminde pivotlari bulur.
            val = self.get(k,j)
            if abs(val) > abs(max_val):
                max_val = val
                max_ind = k
        return max_val,max_ind
 
    def divide_row(self,i,v):        #diziyi indisine gore bolmek icin.
        """divide row i by v"""
        self.map_row(lambda x: x[1]/v,i)
 
    def substract_row(self,i,j):              #dizide cikartma icin.
        """substract all rows by row i column j"""
        for u in range(self.m):
            if u != i:
                self.map_row(lambda x: x[1]-(self.get(u,j)*self.get(i,x[0])),u)
 
class GaussianElimination(Matrix,Solver):    #Gauss indirgemesi icin gereken fonksiyonlarin gauss sinifi olarak toplanmasi.
    def __init__(self,data):        
        m = len(data)
        n = len(data[0])
        Matrix.__init__(self,m,n,data)  #Matrix sinifimizdan miras aliyoruz.Yontem icin matrislere ihtiyac var.
 
    def solve(self):  #İste asil cozme fonksiyonumuz.
        i,j = 0,0    #ilk basta i ve j sifir cunku 
        while i < self.m and j < self.n:
            max_val,max_ind = self.find_pivot(i,j)    #pivot ayarlama kismi
            if max_val != 0:
                self.swap_row(i,max_ind)
                self.divide_row(i,max_val)
                self.substract_row(i,j)
                i += 1
            j += 1
        return [self.get(i,-1) for i in range(self.m)]
 
ms = []
ms += [[[8,7.4,8.225342],
        [7.4,8.72,10.731329]]]
ms += [[[2,1,-1,8],
        [-3,-1,2,-11],
        [-2,1,2,-3]]]
for mi in ms:
    m = GaussianElimination(mi)
    m.show('problem')
    print m.solve()

#ZİNNUR YEŞİLYURT
