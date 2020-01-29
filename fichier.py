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
        self.longueurTexte=0
        
    #creation de la liste alphabet et frquence des elements du texte
    def alphabet(self):
        #on oouvre le fichier
        fichier = open(self.texte,'r')
        #on initialise 2 listes a des listes vides
        alphabet = []
        liste=[]
        
        #☻on parcourt les lignes du fichiers
        for ligne in fichier:
            #on parcourt les caracteres de chaque ligne
            for lettre in ligne:
                #si une lettre n'est pas dans la liste alphabet 
                if lettre not in alphabet:
                    #alors on l'ajoute a notre liste
                    alphabet.append(lettre)
                    #on appelle la methode frequence de ce caractere
                    frequence= self.frequence(lettre)
                    #on ajoute a notre autre liste la frequence correspondant
                    #a ce caractere
                    liste.append((frequence,lettre))
                    
        fichier.close 
        #on retourne la liste composee des caracteres du texte associes a leur
        #frequence triee par ordre croissant de frequence puis par ordre 
        #alphabetique pour des frequences equivalentes
        return sorted(liste)
        
    #methode qui permet de determiner la frequence d'un caractere
    def frequence (self,lettre):
        
        #on ouvre le fichier
        fichier = open(self.texte,'r')
        #on initialise la frequence du caractere a 0
        frequence_caractere=0
        
        #on parcourt les lignes du fichier
        for ligne in fichier:
            #on parcourt les caracteres de chaque ligne
            for caractere in ligne:
                #si le caractere correspond a celui passe en parametre
                if caractere==lettre :
                    #alors on ajoute +1 a la frequence de ce caractere
                    frequence_caractere=frequence_caractere+1
        
        fichier.close
        #on retourne la frequence du caractere passe en parametre
        return frequence_caractere
    
    
    
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
        
    def indexNewArbre(self):
        listeA=[]
        for i in self.listeArbre:
            listeA.append(i)
            
        return listeA
            
        
#    def tauxCompression(self):
#        longTexte=self.longueurTexte*8
#        return(1-len(self.arbre)/longTexte)*100
            


texte= 'textesimple.txt'  
f=Fichier(texte)
print(f.alphabet())
print(f.indexNewArbre())

#print(f.tauxCompression())




