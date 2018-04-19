#¡” «”« 15


#synarthsh pou ypologizei thn seira taylor tou e^x gia dwsmeno n(akriveia)
#kai gia thn dosmenh  x(dynamh)
#to e^x mporoume na to ypologisoume e^x = 1 + x/1! + x^2/2! + x^3/3! + ....
#h alliws e^x = 1 + (x/1) (1 + (x/2) (1 + (x/3) (........) ) )

def ekthetiko(n,x):

    sum=1.0

    for i in range(n,0,-1):
        sum=1+x*sum/i
    return sum


#elegxos ths eisodou tou xrhsth
#an valei string tou vgazei to mynhma 
#na valei ton swsto typo dedomenou

while True:
    try:
        n=int(input("Parakalw eisagetai akeraio gia thn akriveia pou thelete na ypologisete: "))
        break;
    except:
        print("Prospathiste ksana kai eisagete akeraio")


while True:
    try:
        x=float(input("\nParakalw eisagetai thn dynamh tou e^x pou thelete na ypologistete: "))
        break;
    except:
        print("Prospathiste ksana kai eisagetai pragmatiko arithmo ")



print("to apotelesma einai: %.20f" %ekthetiko(n,x))





