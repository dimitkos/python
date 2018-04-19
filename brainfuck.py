#ASKHSH 9


eisodos= raw_input()

#gia ton elegxo an douleyei swsta an valoume to parakatw san eisodo
#++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
#tote tha mas typwsei H e l l o   W o r l d ! 


#desmeyei mia registry 30000 thesewn opou ayto to kanoume me mia lista
#toswn thesewn pou malista thn arxikopoiume na einai h timh 0
#se oles aytes tis theseis
registry = [0] * 30000

#arxikopoioyme ton pointer sthn thesh 0
pointer = 0

i = 0

#twra thn eisodo tou xrhsth tha thn analysoume xarakthra pros xarakthra
while i <= len(eisodos) - 1:
    s = eisodos[i]
    #an ayto pou diavazei einai ">" metaferoume ton deikth mia thesh deksia
    if s == '>':
        pointer += 1
        #sthn peiptwsh opou ftasei h kseperasei to megethos ths listas-registry
        #ton ksanavazoume sthn arxh arxikopoiontas ton 0
        if pointer >= len(registry):
            pointer = 0
    #an to symvolo einai "<" tote o deikths tha metaferthei mia thesh aristera
    elif s == '<':
        pointer -= 1
       #ton deikth ton exoume arxikopoihsh 0,an parei arnhtikh timh tote ton
        #metaferoume sthn teleytaia thesh ths registry
        if pointer < 0:
            pointer = len(registry) - 1
    #an anagnwrisei ton xarakthra "+" tote tha ayksisei thn timh
    #tou trexontos deikth dedomenvn kata ena
    elif s == '+':
        registry[pointer] += 1
    ##an anagnwrisei ton xarakthra "-" tote tha meiwsei thn timh
    #tou trexontos deikth dedomenvn kata ena
    elif s == '-':
        registry[pointer] -= 1
    #se aythn thn periptwsh me to symvolo "." emfanizei thn timh tou
    #tou trexontos deikth dedomenwn
    elif s == '.':
        print chr(registry[pointer]),
    #me to symvolo "," dexetai ton epomeno xarakthra san eisodo gia
    #ton trexonta deikth dedomenwn
    elif s == ',':
        data=raw_input('\n')
        registry[pointer] = ord(data)

    #sthn periptwsh pou exoume "[" tote elegxoume an h timh tou trexonta deikth
    #einai mhden kai metakinoume ton deikth entolwn sthn ] pou tairiazei
    elif s =='[':
        if registry[pointer] == 0:
            loop = 1
            while loop > 0:
                i += 1
                #analioume thn symvoloseira kai elegxoume tis parantheseis
                c = eisodos[i]
                #me ayton ton tropo tairiazoume tis perntheseis me tis katalliles
                #times pou pernoyn ta loop kai otan ginei 0 termatizetai h while
                if c == '[':
                    loop += 1
                elif c == ']':
                    loop -= 1
    #se aythn thn periptwsh pou exoyme "]" epistrefoume ton deikth
    #entolwn sthn "[" pou tairiazei
    #douleyoume paromoia pali opws parapanw gia na vroume tis parentheseis pou tairiazoun
    elif s == ']':
        loop = 1
        while loop > 0:
            i -= 1
            c = eisodos[i]
            if c == '[':
                loop -= 1
            elif c == ']':
                loop += 1
        i -= 1
    i += 1
