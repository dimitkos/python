#ASKHSH 4


#elegxos eisodou ti arithmo tha dwsei o xrhsths

while True:
    try:
        arithmos=int(input("dwse enan akeraio arithmo apo to 1 ews 1000000:"))
        if arithmos>0 and arithmos<=1000000:
            break;
    except:
        print("parakalw dwse akeraio apo 1-1000000:")

#synarthsh pou pernei enan arithmo pou eisagei o xrhsths
#kai to metatrepei sto antistoixo rwmaiko
        
def romaikos(arithmos):

    #ftiaxnoume dyo pleiades (tuples) opou  sthn prwth exoume tous arithmous
    #sthn deyterh tous rwmaikous.einai se sygkekrimenes theseis etsi wste na yparxei 
    #antistoixeia metaksy tous
    akeraioi = (100000,10000,2000,1000, 900,  500, 400, 100,  90, 50, 40, 10,  9, 5, 4, 1)
    romans = ('-C','-X','MM','M',  'CM', 'D', 'CD','C', 'XC','L','XL', 'X','IX','V','IV','I')

    result = ""

    for i in range(len(akeraioi)):
        #vriskei enan akeraio count apo thn diairesh toy arithmou poy edwse o xrhsths
        #me kathe stoixeio ths tuple akeraioi
        count = int(arithmos / akeraioi[i])
        #ton akeraio count pou vrikame ton pollaplasiazoume me ton  rwmaiko pou
        #antistoixei to akeraioi[i] kai ton prosthetoume sto apotelesma result
        result += romans[i] * count
        #telos afairoyme apo ton arithmo tou xrhsth ton prwto megalytero apo 
        #tous akeraious epi to count kai sthn synexeia to apotelesma tha analythei pereterw
        #px to 13 tha ginei 13-10 kai to 3 tha analythei peretairw me thn idia diadikasia
        arithmos -= akeraioi[i] * count
    return result


#ektypwsh apotelesmatos
print("\nO akeraios poy epileksate antistoixei ston rwmaiko:")
print(romaikos(arithmos))

        
   

