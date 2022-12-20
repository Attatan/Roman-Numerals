import math

def roman_conversion():
    number_array = []
    word = ''
    test_case = int(input("Please enter a non-negative, non-zero integer: "))
    test_string = str(test_case)
    for i in range(len(str(test_string))):
        number_array.append(str(test_string[i]))
    for i in range(len(number_array)):
        number_array[-i-1]=int(number_array[-i-1])*10**(i)
    for i in range(len(number_array)):
        word += conwert(number_array[i])
    print(word)


def conwert(integer):
    Roman_array = [['I','V'],['X','L'],['C','D'],['M','']]
    numeral = ''
    x = len(str(integer))-1
    essence = (str(integer)[0])
    ess = int(essence)
    if x < 3:
        if ess == 0:
            numeral = ''
        if 0 < ess < 4:
            numeral = Roman_array[x][0]*ess
        elif ess == 4:
            numeral = Roman_array[x][0] + Roman_array[x][1] 
        elif 4 < ess < 9:
            numeral = Roman_array[x][1]+(ess-5)*Roman_array[x][0]
        elif ess == 9:
            numeral = Roman_array[x][0]+Roman_array[x+1][0]
    else:
        numeral = 'M'*ess*10**(x-3)
    return numeral

roman_conversion()
