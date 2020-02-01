# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 17:28:31 2020

@author: FERRERA
"""

class Arbre:
    
    def __init__(self,valeur,label,filsdroit=None,filsgauche=None):
        self.valeur = valeur
        self.label=label
        self.filsdroit=filsdroit
        self.filsgauche=filsgauche
        self.code=""
        
        
    def get_label(self):
        return self.label
    
    
    def code_profondeur(self,code=""):

        
        self.code=code
        
        if self.filsgauche():
            code = code+"0"
        if self.filsdroit():
            code = code+"1"
        self.code_profondeur(self.filsgauche,code)
            
    
            
    
        
        
            
    
            
    
            