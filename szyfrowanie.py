"""
Zasada działania szyfru:
podany wyraz dzielony jest na części/ sylaby
następnie kolejność elementów jest odwraca
odwrócona kolejność ma jeszcze dodatkowe elementy litery K na początku
i na końcu wyrazu
Tak przygotowany wyraz jest dddawany do tekstu i gotowa do uzycia

"""
def logo():
    print("""
                   _.--.    .--._
                 ."  ."      ".  ".
                ;  ."    /\    ".  ;
                ;  '._,-/  \-,_.`  ;
                \  ,`  / /\ \  `,  /
                 \/    \/  \/    \/
                 ,=_    \/\/    _=,
                 |  "_   \/   _"  |
                 |_   '"-..-"'   _|
                 | "-.        .-" |
                 |    "\    /"    |
                 |      |  |      |
         ___     |      |  |      |     ___
     _,-",  ",   '_     |  |     _'   ,"  ,"-,_
   _(  \  \   \"=--"-.  |  |  .-"--="/   /  /  )_
 ,"  \  \  \   \      "-'--'-"      /   /  /  /  ".
!     \  \  \   \                  /   /  /  /     !
:      \  \  \   \                /   /  /  /      TK

    """)
logo()
def intro():
    print("""
        W okresach napiętej i trudnej dla zakonu niemieckiego sytuacji 
    krzyzacy  w przesyłanej korespondejci stosowali szyfry.
    Szczególnie znana była taka praktyka w okresie urzędowania prokuratora
    zakonu w Rzymie Piotra z Ornety byłego kapelana Wielkiego Mistsza
    w liście skierowanym do niego liscie  Wielkiego Mistsza Michała Kuchmeistra 
    z 26 czerwca 1419 roku.
    """)

intro()
slowo_do_podzialu = input("Podaj wyraz : ").upper()


def podzial_na_sylaby(slowo_do_podzialu):
    
    samogloski = ("A","Ą", "E", "Ę","I","O", "Ó","U" )
    lista_sylab = []
    sylaba = ""
    for x in slowo_do_podzialu:
        if x in samogloski:
            sylaba += x
            lista_sylab.append(sylaba)
            sylaba = ""
        else:
            sylaba += x
    if sylaba:
        lista_sylab.append(sylaba)
    return ",".join(reversed(lista_sylab))


podzial_na_sylaby(slowo_do_podzialu)
def zmiana_wyrazu():
    zaszyfrowany_wyraz = podzial_na_sylaby(slowo_do_podzialu)
    wyraz = zaszyfrowany_wyraz.split(",")
    
    return "".join(wyraz)

zmiana_wyrazu()
def haslo():
    nowy_wyraz = zmiana_wyrazu()
    szyfr = "K" + nowy_wyraz + "K"
    return szyfr


haslo()
def zaszyfrowany_tekst():
    do_tekstu = haslo()
    print(f" Tajne spotkanie jest w {do_tekstu} , wpisz zaszyfrowany wyraz do korespondencji \n")

zaszyfrowany_tekst()    
    
    
