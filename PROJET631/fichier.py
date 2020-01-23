# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:37:27 2020

@author: ferreraa
"""


class Fichier:
    
    def __init__(self,texte):
        self.texte=texte

    def alphabet(self):
        alphabet = []
        new_alphabet=[]
        
        for caractere in self.texte :  
           alphabet.append(caractere)  
           for i in alphabet:
               if i not in new_alphabet:
                   new_alphabet.append(i)
                   
        return sorted(new_alphabet)
        

    def frequence (self):
    
        table_freq = {}
        
        for caractere in self.texte:
            if caractere in table_freq :
                table_freq[caractere]= table_freq[caractere]+1
            else :
                table_freq[caractere]=1
                
        return table_freq
            
  

t=open('test.txt','r')
#line = t.readlines()
#print(line)  


t1=open('textesimple.txt','r') 
test=t1.readline().replace(" ","")   

          
f=Fichier(t2)

print ('alphabet :',f.alphabet())
print('fréquence :',f.frequence())


