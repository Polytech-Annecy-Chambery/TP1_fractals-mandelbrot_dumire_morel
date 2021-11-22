# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

#Partie 2
from math import sqrt

class NombreComplexe:
    """Classe représentant un nombre complexe."""
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        
    def module(self):
        return sqrt((self.real)**2+(self.imag)**2)
    
    def __str__(self):
        ch=''
        if (self.real!=0):
            ch+=str(self.real)
        if (self.imag!=0):
            if (self.imag>0):
                ch+=' + '+str(self.imag)+'i'
            else:
                ch+=' - '+str(abs(self.imag))+'i'
        return ch
    
    def __add__(self,nc):
        return NombreComplexe(self.real+nc.real,self.imag+nc.imag)

    def __sub__(self,nc):
        return NombreComplexe(self.real-nc.real,self.imag-nc.imag)

    def __mul__(self,nc):
        return NombreComplexe(self.real*nc.real-self.imag*nc.imag,self.real*nc.imag+self.imag*nc.real)              
    
    def __pow__(self,n):
        res=self
        for i in range(1,n,1):
            res=res*self
        if (n==0):
            res=NombreComplexe(1,0)
        return res
        
#Question 1 :
A=NombreComplexe(1,10)
B=NombreComplexe(5,-10)
C=NombreComplexe(-3,0)

#Question 2 :
print('Question 2 :',A.module(),B.module(),C.module(),'\n')

#Question 3 : 
print('Question 3 :',A,B,C,'\n')

#Question 4 : 
print('Question 4 - addition :',A+B,B+C,A+C,'\n')
print('Question 4 - soustraction :',A-B,B-C,A-C,'\n')
print('Question 4 - multiplication :',A*B,B*C,A*C,'\n')

#Question 5 :
print('Question 5 :',A**1,B**2,C**3,'\n')

#Partie 3
#Question 1 : Zd = 2-i, pas_x = 3/(n_x - 1) et pas_y = -2/(n_y - 1)

#Question 2 : 
Zd=NombreComplexe(2,-1)
def nombre_complexe(k,l,n_y,n_x):
    return NombreComplexe(l*(3/(n_x - 1))-Zd.real,k*(-2/(n_y - 1))-Zd.imag)

#Question 3 :
def grille_complexe(n_y,n_x):
    grille=[]
    for i in range(0,n_y,1):
        l=[]
        for j in range(0,n_x,1):
            l+=[nombre_complexe(i,j,n_y,n_x)]
        grille+=[l]
    return grille

#Partie 4
import matplotlib.pyplot as plt
import copy
#Question 1 : Cette ligne import une librairie graphique, et lui donne un alias (plt)

#Question 2 : 
n_y = 12 ; n_x = 10
grille = grille_complexe(n_y,n_x)
tableau_module = copy.deepcopy(grille)
for i in range(0,len(tableau_module),1):
    for j in range(0,len(tableau_module[0]),1):
        tableau_module[i][j]=grille[i][j].module()

#Question 3 :
plt.figure()
plt.imshow(tableau_module, aspect='auto')
plt.colorbar()
plt.show()            

#Partie 5
#Question 1 : 
def est_divergente(c,N):
    z=NombreComplexe(0,0)
    cpt=0
    while(cpt<N and z.module()<=2):
        z=z**2+c
        cpt+=1
    return (cpt<N)

#Question 2 :
def image_mandelbrot(n_y,n_x,N):
    grille = grille_complexe(n_y,n_x)
    for i in range(0,len(grille),1):
        for j in range(0,len(grille[0]),1):
            if (est_divergente(grille[i][j],N)==True):
                grille[i][j]=255
            else:
                grille[i][j]=0
    return grille
                
#Question 3 :
image = image_mandelbrot(200,100,20)
plt.figure()
plt.imshow(image, aspect='auto')
plt.colorbar()
plt.show()  

#Question 4 :
#n_y et n_x font varier la résolution de l'image, N influe sur la précision de
#la divergence

#Question 5 : 
#def est_divergente_couleur(c):
#    z=NombreComplexe(0,0)
#    cpt=0
#    while(z.module()<=2):
#        z=z**2+c
#        cpt+=1
#    return [z.module()>2,cpt]
#
#def image_mandelbrot_couleur(n_y,n_x):
#    grille = grille_complexe(n_y,n_x)
#    for i in range(0,len(grille),1):
#        for j in range(0,len(grille[0]),1):
#            tab=est_divergente_couleur(grille[i][j])
#            if (tab[0]==True):
#                grille[i][j]=255
#            else:
#                grille[i][j]=tab[1]
#    return grille
#
#image_couleur = image_mandelbrot_couleur(200,100)
#plt.figure()
#plt.imshow(image_couleur, aspect='auto')
#plt.colorbar()
#plt.show()              
# NON TERMINEE   

#Partie 6
import numpy as np
#Question 1 :
def nombre_complexe_numpy(k,l,n_y,n_x):
    return (l*(3/(n_x - 1))-2)+(k*(-2/(n_y - 1))+1)*j



            
            
            
            
            
            
            