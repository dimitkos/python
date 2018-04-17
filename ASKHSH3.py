#ASKHSH 3


#eisagei protash o xrhsths
protasi=raw_input("parakalw dwste thn protash pou theletai na kwdikopoihsete:")


#synarthsh h opoia pernei mia protash
#kai thn kwdikopoiei symfwna me thn methodo rot 13
def rot13encryption(string):
    
    encrypted=""

    #pernei thn protash pou eisagei o xrhsths kai to kathe gramma
    #to analyei mesw ths ord se enan arithmo pou antistoixei
    #ston pinaka ascii gia to kathe gramma

    for i in string:
        char=ord(i)

    #elegxei an to gramma einai mikro h kefalaio
    #ektelei meta allon enan elegxo an to gramma einai prin h meta to m h M
    #kai to metakinei 13 theseis meta h prin 
        if char >= ord('a') and char <= ord('z'):
            if char > ord('m'):
                char = char-13
            else:
                char=char+13
        elif char >= ord('A') and char <= ord('Z'):
            if char > ord('M'):
                char = char-13
            else:
                char = char+13
        #sthn encrypted twra prosthetei to kathe gramma ksexvrista wste na bgei
        #h kryptografhmenh leksi
        #h chr pernei ton arithmo tou ASCII pou antistoixei to gramma kai to kanei gramma
        encrypted = encrypted + chr(char)

    return encrypted

#emfanizei to kwdikopoihmeno apotelesma ston xrhsth
print("to kwdikopoihmenos mynhma sas einai :")
print(rot13encryption(protasi))
