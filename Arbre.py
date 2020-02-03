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
        self.code =""
        
        
    def get_label(self):
        return self.label
    
    def get_valeur(self):
        return self.valeur
    
    def get_filsgauche(self):
        return self.filsgauche.valeur
    
    def get_filsdroit(self):
        return self.filsdroit.valeur
    
    def parcours_profondeur(self,code=""):
        
        self.code=code
        print(self.code,self.get_label())
        
        if self.filsgauche !=None:
            self.filsgauche.parcours_profondeur(code=code+"0")
        if self.filsdroit != None:
            self.filsdroit.parcours_profondeur(code=code+"1")
        
        return code
    
    
#        for fils in liste_fils :
#            fils.parcours_profondeur()
#            
#    def code(self,code=""):
#        
#        self.code=code
#        
#        if self.filsgauche != None:
#            pass
    
   
         
         
 
    
            
    
            