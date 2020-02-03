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

        
        
    def get_label(self):
        return self.label
    
    def get_valeur(self):
        return self.valeur
    
    def get_filsgauche(self):
        return self.filsgauche.valeur
    
    def get_filsdroit(self):
        return self.filsdroit.valeur
    
    def parcours_profondeur(self,lettre,code=""):

        if lettre==self.label:
            return code
        else:
            if self.filsgauche !=None:
                if self.filsgauche.parcours_profondeur(lettre,code+"0") != None:
                    return self.filsgauche.parcours_profondeur(lettre,code+"0")             
            
            if self.filsdroit != None:
                if self.filsdroit.parcours_profondeur(lettre,code+"1") != None:
                    return self.filsdroit.parcours_profondeur(lettre,code+"1")
            
         
         
 
    
            
    
            