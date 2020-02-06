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
        self.code_bin=""
        
        
    #creation de la liste alphabet et frquence des elements du texte
    def alphabet(self):
        #on oouvre le fichier
        fichier = open(self.texte+".txt",'r')
        
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
        
        #on cree un autre fichier dans lequel apparait la taille de l'alphabet
        #et la frequence associee a chaque caractere
        with open(self.texte+"_freq.txt","w") as f :
            f.write("Taille de l\'alphabet:"+str(len(liste))+"\n")
            for elem in sorted(liste):
                f.write(str(elem)+"\n")
            
        fichier.close 
        #on retourne la liste composee des caracteres du texte associes a leur
        #frequence triee par ordre croissant de frequence puis par ordre 
        #alphabetique pour des frequences equivalentes
        return sorted(liste)
        
    #methode qui permet de determiner la frequence d'un caractere
    def frequence (self,lettre):
        
        #on ouvre le fichier
        fichier = open(self.texte+".txt",'r')
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
    
    def dictionnaire(self):
        dictionnaire={}
        
        for (freq,alpha) in self.liste_afreq:
            dictionnaire[alpha]=self.listeArbre[0].parcours_profondeur(alpha)
        print(dictionnaire)
        return dictionnaire
    
    #on cree les feuilles
    def creation_feuille(self):
        liste_afreq=self.alphabet()
        #on parcourt les tuples (frequences,caractere) present dans la liste
        #(frequence,alphabet)
        #print("les feuilles",liste_afreq,"\n")
        for (freq,alpha) in liste_afreq:
            #on ajoute a la liste des arbres chaque tuple en creant un arbre 
            #a partir de chaque tuple
            self.listeArbre.append(Arbre(freq,alpha))
            
        return self.listeArbre
     
    #on cree l'arbre
    def arbre(self):
        self.creation_feuille()
        #tant qu'il ne reste pas un seul element dans la liste des arbres
        while(len(self.listeArbre)!=1):
            #on appelle la methode creationArbre()
            self.creationArbre()
        
        self.dictionnaire()
        self.affichage_code()
        
    
    
    def affichage_code(self):
        dico=self.dictionnaire()
        #ouverture du fichier
        fichier = open(self.texte+".txt",'r')
        
        liste_bin=[]
        #on parcourt les lignes du fichier
        for ligne in fichier:
            #on parcourt les caracteres de chaque ligne
            for caractere in ligne:
                liste_bin.append(dico[caractere])
        
        resul=''
        for chiff_bin in liste_bin:
             resul = resul + str(chiff_bin)
        
        
        if (len(resul)%8)==0:
        
            resulfin =  [resul[i:i+8] for i in range (0,len(resul),8)]
        else:
            while(len(resul)%8)!=0:
                resul=resul+'0'
            resulfin =  [resul[i:i+8] for i in range (0,len(resul),8)]
        
        resultatFinal=''
        for chiff_fin in resulfin:
            resultatFinal = resultatFinal + str(chiff_fin)
        print(self.tauxCompression(len(resultatFinal)))
        
        int_bin=[]
        for i in resulfin:
            int_bin.append(int(i,2))
            
        

                  
        '''Convertir la chaine en int pour ensuite faire (int).to_bytes(1,byteorder)''' 
        with open(self.texte+"_comp.bin","wb") as f:
            for j in int_bin:
                #j_byte=str.encode(j)
                j_byte=(j).to_bytes(1,byteorder='big')
                f.write(bytes(j_byte))
                
        fichier.close
  
    def tauxCompression(self,longBin):
        volIni=0
        fichier = open(self.texte + ".txt","r")
        texte = fichier.read()
        volIni = len(texte)*8
        
        volFin = longBin
        print('volinitial',volIni)
        print('volfinal',volFin)
        return(1-volFin/volIni)*100
        
        
    def creationArbre(self):
        
        
        
        ab1=self.listeArbre[0]
        ab2=self.listeArbre[1]
        
        
        arbre=Arbre(ab1.valeur+ab2.valeur,'',ab1,ab2)
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
        
        index=self.indexNewArbre(arbre)
        self.listeArbre[index:index]=[arbre]
       
        
    #methode qui permet de determiner l'index correspondant a l'endroit 
    #d'insertion de l'arbre dans la liste des arbres
    def indexNewArbre(self,nouvelArbre):
        #on cree une liste vide
        listeA=[]
        #on parcourt les arbres de la liste arbres
        for arbre in self.listeArbre:
            #on ajoute dans la liste vide le tuple (valeur,etiquette) de chaque
            #arbre de la liste des arbres
            listeA.append((arbre.valeur,arbre.label))
        #on ajoute dans cette liste les valeurs du tuple de l'arbre passe en
        #parametre
        listeA.append((nouvelArbre.valeur,nouvelArbre.label))
        #on tri cette liste
        #on retourne l'index de l'arbre passe en parametre correspondant a sa
        #place dans le liste cree initialement      
        print(sorted(listeA))
        
        return sorted(listeA).index((nouvelArbre.valeur,nouvelArbre.label))
            
        
            


texte= 'alice'  
f=Fichier(texte)
#print("l'alphabet  ",f.alphabet(),"\n")
p=f.arbre()
#f.stockage()
#print(f.tauxCompression())




