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
        
        
    #creation de la liste alphabet et frquence des elements du texte
    def alphabet(self):
        #on oouvre le fichier
        fichier = open(self.texte+".txt",'r')
        
        #on initialise 2 listes a des listes vides
        alphabet = []
        liste=[]
        
        #on parcourt les lignes du fichiers
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
        print('liste triee',sorted(liste))
        #on cree un autre fichier dans lequel apparait la taille de l'alphabet
        #et la frequence associee a chaque caractere
        with open(self.texte+"_freq.txt","w") as f :
            f.write("Taille de l\'alphabet:"+str(len(liste))+"\n")
            for (fr,c) in sorted(liste):
                f.write(str(fr)+' ')
                f.write(c+'\n')

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
   
    #on cree un dictionnaire
    def dictionnaire(self):
        #on l'initialise a vide
        dictionnaire={}
        
        #on parcourt la liste des frequences et des lettres
        for (freq,alpha) in self.liste_afreq:
            #on ajoute le code correspondant a chaque caractere de l'alphabet 
            #avec le parcours en profondeur
            dictionnaire[alpha]=self.listeArbre[0].parcours_profondeur(alpha)
        
        #on affiche le dictionnaire
        print(dictionnaire)
        return dictionnaire
    
    #on cree les feuilles
    def creation_feuille(self):

        #on parcourt les tuples (frequences,caractere) present dans la liste
        #(frequence,alphabet)
        #print("les feuilles",liste_afreq,"\n")
        for (freq,alpha) in self.liste_afreq:
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
        
        #on appelle la methode permettant l'affichage du code du texte
        self.affichage_code()
        
    
    
    def affichage_code(self):
        
        #on appelle le dictionnaire
        dico=self.dictionnaire()
        #ouverture du fichier
        fichier = open(self.texte+".txt",'r')
        
        #on initialise une liste a vide
        liste_bin=[]
        #on parcourt les lignes du fichier
        for ligne in fichier:
            #on parcourt les caracteres de chaque ligne
            for caractere in ligne:
                #on ajoute dans la liste les codes de chaque caractere
                liste_bin.append(dico[caractere])
        
        #on initialise un resultat a une chaine vide
        code_bin=''
        #on parcourt la liste des codes
        for chiff_bin in liste_bin:
            #on ajoute tous les codes de chaque caractere pour afficher un code total
             code_bin = code_bin + str(chiff_bin)
        
        
        liste_octet=self.decoupage_octet(code_bin)
        
        #concatenation du code binaire
        #on initialise un resultat final a une chaine vide
        codeFinal=''
        #on parcourt la liste de nos octets
        for chiff_fin in liste_octet:
            #on ajoute tous nos octets les uns a la suite des autres
            codeFinal = codeFinal + str(chiff_fin)
        
        #on affiche le taux de compression de notre resultat final 
        print('Taux de compression',self.tauxCompression(len(codeFinal)),'%')
        
        #on converti les codes des caractreres en entier
        #exemple : 00001001 = 9, on ajoute tous ces entiers dans une liste
        int_octet=[]
        for i in liste_octet:
            int_octet.append(int(i,2))
             
        #on cree un fichier binaire dans lequel on place le texte compresse
        with open(self.texte+"_comp.bin","wb") as f:
            #on parcourt notre liste de nos entiers
            for entier in int_octet:
                #on converti les entiers en octet
                byte=(entier).to_bytes(1,byteorder='big')
                f.write(bytes(byte))
                
        fichier.close
  
    def decoupage_octet(self,liste):
        
        resultat =[]
        #on veut decouper le code total en octet
        #si la longueur du resultat total est divisible par 8
        if (len(liste)%8)==0:
        
            #alors on separe le code total 8 par 8 (en octet) que l'on stocke dans une variable
            resultat =  [liste[i:i+8] for i in range (0,len(liste),8)]
        
        #si c'est pas divisible par 8
        else:
            #tant que la longueur du texte n'est pas divisible par 8
            while(len(liste)%8)!=0:
                #on ajoute des 0 au code
                liste=liste+'0'
            #on separe 8 par 8 le code que l'on stocke dans une variable
            resultat =  [liste[i:i+8] for i in range (0,len(liste),8)]
        return resultat
        
    #○methode permettant de calculer le taux de compression d'un fichier
    def tauxCompression(self,longBin):
        #on initialise un volume initial a 0
        volIni=0
        #on ouvre le fichier texte
        fichier = open(self.texte + ".txt","r")
        #on lit ce fichier
        texte = fichier.read()
        
        #on multiplie la longueur total du texte par 8 car chaque caractere
        #est code sur 8 bits
        volIni = len(texte)*8
        
        #le volume final correspond a la longueur donne en parametre
        volFin = longBin
        
        print('volinitial du fichier en bits',volIni)
        print('volfinal du fichier en bits ',volFin)
        
        #on retourne le taux de compression en pourcentage qui correspond a 
        #1-volumefinal/volumeinitial
        return(1-volFin/volIni)*100
        
    #methode qui cree l'abre
    def creationArbre(self):
        
        #on recupere les deux arbres les plus petits de la liste, ce qui correspond
        #aux arbres a la premiere et deuxieme places dans la liste
        ab1=self.listeArbre[0]
        ab2=self.listeArbre[1]
        
        #on cree un nouvel arbre qui prend en frequence la somme des deux arbres
        #en label une chaine vide et en fils gauche le plus petit des 2 et en fils
        #droit le plus grand
        arbre=Arbre(ab1.valeur+ab2.valeur,'',ab1,ab2)
        #on enleve de la liste des arbres le plus grand des 2 puis le plus petit
        self.listeArbre.pop(1)
        self.listeArbre.pop(0)
        
        #on recherche l'index correspond au nouvel arbre precedemment cree
        index=self.indexNewArbre(arbre)
        #on ajoute dans la liste arbre a sa place le nouvel arbre
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
            
        
            






