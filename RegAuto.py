from MyMoodle import *

salasõnad=loe_faelist("salasõnad.txt")
kasutajanimed=loe_faelist("kasutajad.txt")
while True:
    print(kasutajanimed)
    print(salasõnad)
    print("1-registreerimine\n2-autoriseerimine\n3-nime või parooli muutmine\n4-unustanud parooli taastamine\n5-lõpetamine")
    vastus=int(input("Sissestage arv "))
    if vastus==1:
        print("Registreerimine")
        kasutajanimed,salasõnad=registreerimine(kasutajanimed, salasõnad)
    elif vastus==2:
        print("Autoriseerimine")
        autoriseerimine(kasutajanimed,salasõnad)
    elif vastus==3:
        print("Nime või parooli muutmine")
        vastus=input("Kas muudame nime või paooli: ")
        if vastus=="nimi":
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
        elif vastus=="parool":
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
        elif vastus=="mõlemad":
            print("Nime muutmine")
            kasutajanimed=nimi_või_parooli_muurmine(kasutajanimed)
            print("Parooli muutmine")
            salasõnad=nimi_või_parooli_muurmine(salasõnad)
    elif vastus==4:
        print("Unustanud parooli taastamine: ")
        salasõnad=genereerida_parooli(8)
    elif vastus==5:
        print("Lõpetamine")
        kirjuta_failisse("kasutajad.txt",)
        kirjuta_failisse("salasõnad.txt",salasõnad)
        break
    else:
        print("Tunmatu valik")
