# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:28:31 2020

@author: FERRERA
"""

class Arbre:
    
    def __init__(self,valeur,label,filsgauche=None,filsdroit=None):
        self.valeur = valeur
        self.label=label
        self.filsdroit=filsdroit
        self.filsgauche=filsgauche

        
    #on realise le parcours en profondeur de l'arbre pour un caractere donne en
    #parametre
    def parcours_profondeur(self,lettre,code=""):
        
        #si le caractere est correspond au noeud sur lequel on est
        if lettre==self.label:
            #alors on retourne le code
            return code
        #sinon
        else:
            #si le fils gauche existe
            if self.filsgauche !=None:
                #si le parcours en profondeur depuis le fils gauche est possible
                if self.filsgauche.parcours_profondeur(lettre,code+"0") != None:
                    #on ajoute un 0 au code
                    return self.filsgauche.parcours_profondeur(lettre,code+"0")             
            #si le fils droit existe
            if self.filsdroit != None:
                #si le parcours en profondeur depuis le fils droit est possible
                if self.filsdroit.parcours_profondeur(lettre,code+"1") != None:
                    #on ajoute 1 au code
                    return self.filsdroit.parcours_profondeur(lettre,code+"1")
            
         
         
 
    
            
    
            