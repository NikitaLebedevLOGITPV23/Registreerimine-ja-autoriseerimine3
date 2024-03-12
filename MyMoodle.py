from string import *
from random import *
import random
import string
from typing import List
from time import sleep
from os import path, remove
def registreerimine(kasutajad:list,paroolid:list)->any:
    """Funktsioon tagastab 2 listid
    :param list kasutaja: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    :rtype: list,list
    """
    while True:
        nimi=input("Mis on sinu nimi on? ")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool? ")
                flag_p=False
                flag_l=False
                flag_u=False
                flag_d=False
                if len(parool)>=8:
                    parool_list=list(parool)
                    for p in parool_list:
                        if p in punctuation:
                            flag_p=True
                        elif p in ascii_lowercase:
                            flag_l=True
                        elif p in ascii_uppercase:
                            flag_u=True
                        elif p in digits:
                            flag_d=True
                    if flag_p and flag_u and flag_l and flag_d:
                        kasutajad.append(nimi)
                        paroolid.append(parool)
                    break
                else:
                    print("Nõrk salasõna!")
            break
        else:
             print("Selline kasutaja on juba olemasi! ")
        return kasutajad, paroolid
def autoriseerimine(kasutajad:list,paroolid:list):
    """Funktsioon kuvab ekraanile "Tere tulemas! kui kasutaja on olemas nimekirjas
    Niki on järjendis kasutajad
    Salasõna on paroolide järjendis
    Nimi ja salasõna indeksid on võrdsed
    :param list kasutajad: Kasutaja nimede kirjeldus
    :param list paroolid: Kasutaja nimed paroolid
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        if nimi in kasutajad:
            parool=input("Sesesta salasõna: ")
            while True:
                p+=1
                try:
                    if kasutajad.index(nimi)==paroolid.index(parool):
                       print(f"Tere tulemast! {nimi}")
                       break
                except:
                    print("Vale nimi või salassõna!")
                    if p==5:
                        print("Proovi uuesti 10 sek pärast")
                        for i in range(10):
                            sleep(1)
                            print(f"On jäänud {10-i} sek")
        else:
             print("Kasutajat pole")
def nimi_või_parooli_muurmine(list_:list):
    """
    """
    muutuja=input("Vana nimi või parool: ")
    if muutuja in list_:
        indeks=list_.index(muutuja)
        muutuja=input("Uus nimi või parool: ")
        list_[indeks]=muutuja
    return list_
def genereerida_parooli(length:int)-> str:
    """Funktsioon loob parooli
    Looge etteantud pikkusega parool.
    """
    result:List[str]=[]
    choices=string.ascii_letters+string.digits
    while len(result)<length:
         symbol=random.choice(ascii_letters+string.digits)
         result.append(symbol)
    return "".join(result)
def loe_faelist(fail:str)->list:
    """Funktsioon loeb tekst *.txt failist
    """
    f=open(fail,"r",encoding="utf-8")
    salasõnad=[]
    for rida in f:
        salasõnad.append(rida.strip())
    f.close()
    return salasõnad
def kirjuta_failisse(fail:str,salasõnad=[]):
    """Salvestame tekst failisse
    """
    #n=int(input("Mitu: "))
    #for i in range(n):
    #    järjend.append(input(f"{i+1}. sõna: "))
    f=open(fail,"w",encoding="utf-8")
    for element in salasõnad:
        f.write(element+"\n")
    f.close()
def ümber_kirjuta_fail(fail:str):
    """
    """
    f=open(fail,"a")
    text=input("Sissesta tekst:")
    f.write(text+"\n")
    f.close
def failide_kustutamine():
    """
    """
    failnimi=input("Mis fail tahad eemaldada?") #path.isdir("Kaust")
    if path.isfile(failnimi):
        remove(failnimi)
        print(f"Fail {failnimi} oli kustutatud")
    else:
        print(f"Fail {failnimi} oli puudub")