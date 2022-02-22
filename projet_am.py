import csv
import string

#import re
ALPHA = string.ascii_letters
f = open(r'donnees_projet.csv', 'r')
reader= csv.reader(f)
#for row in reader:
      #print(row)
headers = next(reader, None)

#print(headers)
column = {}
for h in headers:
   # print(h)
    column[h] = []
  
#print(column)
for row in reader:
    #print(row)
    fonct = {h: v for h, v in zip(headers, row)}
    #print(fonct)
    def numero_valide(numero):
           if len(fonct["Numero"]) == 7 and fonct["Numero"].isalnum() and (not fonct["Numero"].isalpha()) and (not fonct["Numero"].isnumeric()) and fonct["Numero"].isupper() == True:
                print( fonct["Numero"])
           else:
                print('invalide')
    numero_valide(fonct["Numero"])
    def prenon_valide(prenom):
        if fonct["Prénom"].startswith(tuple(ALPHA)) and len(fonct["Prénom"]) >= 3 and fonct["Prénom"].isalpha():
            print(fonct["Prénom"])
        else:
            print("invalide")
    prenon_valide(fonct["Nom"])
    
    
    
    def nom_valide(nom):
        if fonct["Nom"].startswith(tuple(ALPHA)) and len(fonct["Nom"]) >= 2 and fonct["Nom"].isalpha():
            print(fonct["Nom"])
        else:
            print("invalide")
    nom_valide(fonct["Nom"])
    
    
    
    def transforme_classe(classe):
        if fonct["Classe"] == '6 eme A' or fonct["Classe"] == '6 em A' or fonct["Classe"] == '6eme A' or fonct["Classe"] == '6em A' or fonct["Classe"] == '6eme A' or fonct["Classe"] == '6 e A'or fonct["Classe"] == '6e A' or fonct["Classe"] == '6emeA' or fonct["Classe"] == '6ieme A'  or fonct["Classe"] == '6iemeA' :
            print('6em A')
        elif fonct["Classe"] == '6 eme B' or fonct["Classe"] == '6 em B' or fonct["Classe"] == '6eme B' or fonct["Classe"] == '6em B' or fonct["Classe"] == '6eme B' or fonct["Classe"] == '6 e B'or fonct["Classe"] == '6e B' or fonct["Classe"] == '6emeB' or fonct["Classe"] == '6ieme B' or fonct["Classe"] == '6iemeB' :
            print('6em B')
        elif fonct["Classe"] == '5 eme A' or fonct["Classe"] == '5 em A' or fonct["Classe"] == '5eme A' or fonct["Classe"] == '5em A' or fonct["Classe"] == '5eme A' or fonct["Classe"] == '5 e A'or fonct["Classe"] == '5e A' or fonct["Classe"] == '5emeA' or fonct["Classe"] == '5ieme A' or fonct["Classe"] == '5iemeA':
            print('5em A')
        elif fonct["Classe"] == '5 eme B' or fonct["Classe"] == '5 em B' or fonct["Classe"] == '5eme B' or fonct["Classe"] == '5em B' or fonct["Classe"] == '5eme B' or fonct["Classe"] == '5 e B'or fonct["Classe"] =='5e B'  or fonct["Classe"] == '5emeB' or fonct["Classe"] == '5ieme B' or fonct["Classe"] == '5iemeB':
            print('5em B')
        elif fonct["Classe"] == '4 eme A' or fonct["Classe"] == '4 em A' or fonct["Classe"] == '4eme A' or fonct["Classe"] == '4em A' or fonct["Classe"] == '4eme A' or fonct["Classe"] == '4 e A'or fonct["Classe"] == '4e A' or fonct["Classe"] == '4emeA' or fonct["Classe"] == '4ieme A'  or fonct["Classe"] == '4iemeA':
            pass#print('4em A')
        elif fonct["Classe"] == '4 eme B' or fonct["Classe"] == '4 em B' or fonct["Classe"] == '4eme B' or fonct["Classe"] == '4em B' or fonct["Classe"] == '4eme B' or fonct["Classe"] == '4 e B'or fonct["Classe"] =='4e B' or fonct["Classe"] == '4emeA' or fonct["Classe"] == '4ieme A'  or fonct["Classe"] == '4iemeB':
            print('4em B')
        elif fonct["Classe"] == '3 eme A' or fonct["Classe"] == '3 em A' or fonct["Classe"] == '3eme A' or fonct["Classe"] == '3em A' or fonct["Classe"] == '3eme A' or fonct["Classe"] == '3 e A'or fonct["Classe"] == '3e A' or fonct["Classe"] == '3emeA' or fonct["Classe"] == '3ieme A' or fonct["Classe"] == '3iemeA':
            print('3em A')
        elif fonct["Classe"] == '3 eme B' or fonct["Classe"] == '3 em B' or fonct["Classe"] == '3eme B' or fonct["Classe"] == '3em B' or fonct["Classe"] == '3eme B' or fonct["Classe"] == '3 e B'or fonct["Classe"] =='3e B' or fonct["Classe"] == '3emeA' or fonct["Classe"] == '3ieme A'  or fonct["Classe"] == '3iemeB':
            print('3em B')
        else: 
            print("invalide")
    transforme_classe(fonct["Classe"])
    
    
    def note_valide(note):
        if "[" in fonct['Note'] and "]" in fonct['Note'] and ";" in fonct['Note'] and ":" in fonct['Note'] and "#" in fonct['Note']:
            pass#print(fonct["Note"])
        else:
            pass#print("invalide")
    note_valide(fonct["Note"])
    
    
    der =  fonct["Note"].replace("#",' ')
    #print(der)
    dump = der.replace('[',' ').replace(']',' ').replace(';',',').replace(':',',')
    #print(dump)
    dum = dump.replace('  ','')
    carz = dump.split()
    #print(carz)
    def sousbliste(lst, n):
        sub=[] ; result=[]
        for i in lst:
           sub+=[i]
           if len(sub)==n: result+=[sub] ; sub=[]
        if sub: result+=[sub]
        return result
    deuf = sousbliste(carz,2)
    
    
    bac = dict(deuf)
    #print(bac)
    
    for key in bac:
        s = bac[key]
        bac[key] = [int(item) for item in s.split(',')]
    print(bac)
    
    moyDict = {}
    for k,v in bac.items():
        moyDict[k] = sum(v)/ float(len(v))
    #print(moyDict)
    moyGob = sum(moyDict.values())/len(moyDict)
    print(moyGob)
    
    
    
    