# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 08:37:27 2020

@author: ferreraa
"""
from Arbre import Arbre

class Fichier:
    
    def __init__(self,texte):
        self.texte=texte
        self.liste_afreq=self.alphabet()
        self.listeArbre=[]

    def alphabet(self):
        fichier = open(self.texte,'r')
        alphabet = []
        liste=[]
        
        
        for ligne in fichier:
            for lettre in ligne:
                if lettre not in alphabet:
                    alphabet.append(lettre)
                    frequence= self.frequence(lettre)
                    liste.append((frequence,lettre))
                    
        fichier.close  
        return sorted(liste)
        

    def frequence (self,lettre):
    
        fichier = open(self.texte,'r')
        compteur=0
        
        for ligne in fichier:
            for caractere in ligne:
                if caractere==lettre :
                    compteur=compteur+1
        
        fichier.close
        return compteur
    
    def creation_feuille(self):
        for (freq,alpha) in self.liste_afreq:
            self.listeArbre.append(Arbre(freq,alpha))
            
    def arbre(self):
        while(len(self.listeArbre)!=1):
            self.creationArbre()
            #self.drawArbre()
    
    def creationArbre(self):
        
        ab1=self.listeArbre[0]
        ab2=self.listeArbre[1]
        
        arbre=Arbre('',ab1.valeur+ab2.valeur,ab2,ab1)
        
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
        index=self.indexNewArbre(arbre)
        self.listeArbre[index:index]=[arbre]
            


texte= 'alice.txt'  
f=Fichier(texte)
print(f.alphabet())




