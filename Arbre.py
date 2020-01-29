# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:28:31 2020

@author: FERRERA
"""

class Arbre:
    
    def __init__(self,label,valeur,filsdroit=None,filsgauche=None):
        self.valeur = valeur
        self.label=label
        self.filsdroit=filsdroit
        self.filsgauche=filsgauche
        
        
    def get_label(self):
        return self.label
    
    
    def parcours_profondeur(self):
        
        print(self.get_label())
        liste_fils=[]
        liste_fils.append(self.filsdroit)
        liste_fils.append(self.filsgauche)
        
        for child in liste_fils:
            child.parcours_profondeur()
            
    def code(self,lettre,code=None):
        
        if self.label==lettre:
            return None
        
        else:
            
            if self.filsgauche!=None:
                return self.code(self.filsgauche,code+1)
            
            if self.filsdroit != None:
                return self.code(self.filsdroit,code+0)
            
    
            