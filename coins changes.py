#ASKHSH 16

#se ayto to programma exv metatrepsei ola ta posa apo eyrv se cents kai kanw tis prakseis

#elegxos sthn plhktrologhsh toy xrhsth gia na mhn dwsei gramma h poso ektow oriwn
while True:
    try:
        plirwmi = float(input('Parakalw eisagete to apaitoumeno poso: '))
        if plirwmi>=0 and plirwmi<=50:
            break;
    except:
        print("Den pliktrologhsate swsta to apaitoumeno poso.Prospathiste ksana")


#oti poso eisagei o xrhsths to metatrepw cents gia eykolia praksewn
payment=plirwmi*100

#orismos poso kanei to eishthrio se cents
ticket = 120

#mia lista opou yparxoyn ola ta kermata opou exoyn metatrapei se cents 
kermata = [200, 100, 50, 20, 10]

#lista h opoia tha thn xrhsimopoihsoyme gia ektypwsh gia na emfanizetai kompsa 
a=['2eyro','1eyro','0.5eyro','0.2eyro','0.1eyro']

#kenh lista poy tah thn xrhsimopoiouse sthn synexeia
b=[]

#ypologizei to poso pou tha prepei na dwsei resta ston pelath
change = payment - ticket


#elegxei to apotelesma twn parapanw praksewn kai ti periptwseis mporei an exei

if change == 0.0:
    print('Den exete resta parakalw perimente na typwthei to eishthrio sas')

elif change < 0:
    ypoloipo = ticket - payment
    print('Parakalw eisagetai akoma %d cents' %int(ypoloipo))

else:
    for i in kermata:
        coins=int(change/i)
        change=change-coins*i
        #prosthetw sthn kenh lista tvn arithmo twn kermatwn tis kathe aksias
        b.append(coins)
        
    #sthn lista a exw thn aksia twn kermatwn kai sthn  
    #sthn lista b exw posa kermata ths kathe aksias antistoixoyn
    #twra ginetai mia kompsi ektypwsh kai twn dyo listwn mazi 
    resta = "\n".join("{} {}".format(x, y) for x, y in zip(b, a))

    print("Ta resta sas einai:")
    print(resta)
