#ASKHSH 17



#eisagoume thn random kai ths dinoume pseydonimo rn
import random as rn

#eisagoume thn time kai ths dinoume pseydonimo tm
import time as tm


#synarthsh h opoia typwnei to tamplo tis trilizas opou o ypologisths kai paikths
# mporoyn na topothetoun ta X,O

def tablo(theseis):
    print "\n"
    print " ", theseis[0], "|", theseis[1], "|", theseis[2]
    print " ---+---+---"
    print " ", theseis[3], "|", theseis[4], "|", theseis[5]
    print " ---+---+---"
    print " ", theseis[6], "|", theseis[7], "|", theseis[8]
    print "\n"


#synarthsh h opoioa dexetai san parametrous ton paikth player
#pou exei seira na paiksei kai tis theseis ths trilizas
#kai epistrefei thn thesh pou epelekse o paikths

def readPosition(player, theseis):
    
    #emfanizetai ksana to tablo ths trilizas aythn thn fora arithmimeno
    #etsi wste na mporei o paikths na epileksei se poio shmeio thelei na kanei epilogh
    tablo(theseis)
    tablo(range(9))
    
    #bazoume elegxous etsi wste o paikths na mhn mporei na plhltrologhsh thesh
    #opou den yparxei h einai kateilhemnh kai tou vgazei ta katallhla mynhmata
    while True:
        
        #epilogh tou paikth pou tha paiksei
        print player, "Dialekse tetragwno:"
        position = int(input())
        if position < 0 or position > 8:
            print "Epelekse timh metaksy tou 0 kai 8!"
        elif theseis[position] != " ":
            print "To", position, " pou epileksate den einai keno."
        else:
            break
    return position


#synarthsh h opoia emfanizei thn kinhsh tou paikth se sygkekrimenh thesh
#pos einai h thesh pou paizei o paikths

def play(player, pos, theseis):

    print "O paikths", player, "paizei sto:", pos
    
    #simplirwsh ths theshs pou epilexthke
    theseis[pos] = player

#synarthsh h opoia elegxei an yparxei triada pou thn katalamvanei enas paikths

def elegxos(player, theseis):

    for triple in triades:
        #me thn entolh ayth oi times tis tuple apothikeyontai stis metavlites
        a, b, c = triple
        # elegxei an o paikths exei katalavei mia triada
        if theseis[a] == theseis[b] == theseis[c] == player:
            return True
   
    return False

#synarthsh h opoia kanei to programma na skeftetai eksypna kai oxi apla na
#gemizei sthn tyxh kena
#elegxei an o paikths exei syplhrwsei tis 2 theseis apo tis treis mias triadas 
#kai epistrefei poia einai kenh,an den yparxei epistrefei none

def elegxosdiadas(player, theseis):

    for triple in triades:
        
        a, b, c = triple
        #an o paikthw katexei 2 apo tis 3 theseis
        if (theseis[a] == theseis[b] == player and
            theseis[c] == " "):
            return c
        elif (theseis[a] == theseis[c] == player and
            theseis[b] == " "):
            return b
        elif (theseis[b] == theseis[c] == player and
            theseis[a] == " "):
            return a
    
    return None


#synarthsh h opoia epistrefei ton paikth poy exei seira na paiksei

def epomenos(player):

    if player == "X":
        return "O"
    else:
        return "X"

#synarthsh h opoia ftiaxnei mia lista me tis diathesimes theseis
    
def available(theseis):

    return [s for s in range(9) if theseis[s] == " "]

#synarthsh h opoia gia ton paikth x toy ypologizei poy na paiksei gia na kanei triliza
#h na mplokarei thn triliza tou antipalou h apla na epileksei ena tyxaio shmeio

def randomPosition(theseis):

    #metraei poses fores exei paiksei o paikths x
    kiniseis = theseis.count("X")
    #sthn periptwsh opou exei paiksei panw apo 2 fores
    if kiniseis >= 2:
        #ginetai elegxos an mporei na kanei triliza o paikths x
        position = elegxosdiadas("X", theseis)
        if position is not None:
            return position
        #elegxei an mporei o paikths O na kanei triliza
        position = elegxosdiadas("O", theseis)
        if position is not None:
            return position
    #se aythn thn periptwsh epilegei mia tyxaia thesh
    return rn.choice(available(theseis))



#vgazei mynhma ston paikth oti ksekinaei to paixnidi
#me thn sleep "pagwnoyme" to programma gia 2 deytera pou exoume orisei

print "-------------------------------------------------------------"
print "\tEisai etoimos na paiksoume triliza?"
print "\n"
tm.sleep(1)



print "\t\tKsekiname!!"
print "-------------------------------------------------------------"
print "\n"
tm.sleep(2)



#orizoume mia pleiada (tuple) opou mesa ths periexei oles tis triades
#oi opoies mporoun na dhmiourghsoun triliza

triades = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))            



#mia lista kenh me 9 theseis kenes arxika opou thn xrhsimopoioume
#gia na anaparistoyme tis 9 theseis tis trilizas 
theseis = 9 * [" "]

#kathorizoume ton paikth pou tha paiksei prwtos
player = "X"

#kai anathetoume sto programma mas na kateythinei aytos ton paikth X
computer = "X"

#to plithos twn kenwn thesewn pou ypoloipontai sthn triliza
#arxika thn arxikopoioume 9 giati prin paikei o ypologisths tha yparxoun 9 kenes theseis
kena = 9

#boolean metavliti pou tha mas deixnei an exei ginei triliza
#thn arxikopoioume false dioti sthn arxh tou paixnidiou den ginetai an exei ginei triliza
triliza = False


#to while ekteleitai oso yparxoyn akoma kena kai den exei ginei triliza

while kena > 0 and not triliza:
    if player == computer:
        # επιλογή θέσης από το πρόγραμμα
        position = randomPosition(theseis)
    else:
        # επιλογή θέσης από τον παίκτη
        position = readPosition(player, theseis)

    #symplirwsh ths epilegmenhs theshs
    play(player, position, theseis)
    
    #meiwnei tis kenes theseis kata ena
    kena -= 1
    
    #elegxos gia triliza
    triliza = elegxos(player, theseis)
    
    #enallagh paikth
    player = epomenos(player)

#emfanizei to teliko tamplo tou pinaka ths trilizas
tablo(theseis)

#anakoinvnei to apotelesma analoga an yparxei nikhths h isopalia
#logo tou tropou enallaghs  tou player typwnoume ton epomenos(palyer) na
#typwnetai o swstos nikhths
if triliza:
    print "Triliza!! Kerdise o", epomenos(player)
else:
    print "Isopalia!Den yparxei nikhths!"

