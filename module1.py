from MyMoodle import *

failide_kustutamine()

ümber_kirjuta_fail(input("Faili nimi: "))

kirjuta_failisse("kasutajad.txt","salasõnad.txt")

salasõnad=loe_faelist("salasõnad.txt")

print(salasõnad)
for sõna in salasõnad:
    print(salasõnad)

