'''
Created on Nov 9, 2012

@author: Joe Lee
'''
#Algorith Referenced from http://en.literateprograms.org/Huffman_coding_%28Python%29
from file_input import File_Input
from huffman import Huffman
import math
import copy

def main():
    input= File_Input()
    huff = Huffman()
    freqTable = input.read()
    huffTable = huff.to_huffman(copy.copy(freqTable))
    str = input.get_str()
    
    binStr = get_bin(huffTable, str)
    results(str, binStr, huffTable)
    menu(freqTable, huffTable, str, binStr)
    
def menu(freqTable, huffTable, str, binStr):
    cont = True
    while cont:
        print("\n------------MENU-------------")
        print("1. Display Frequency Table")
        print("2. Display Binary Table")
        print("3. Display Original File")
        print("4. Display Compressed File")
        print("5. Display Results Again")
        print("0. Exit")
        choice = input("PLease Select An Option: ")
        try:
            opt = int(choice)
        except:
            opt = 10
        print()
        
        if opt == 1:
            print_freq(freqTable)
        elif opt == 2:
            print_table(huffTable)
        elif opt == 3:
            print(str)
        elif opt == 4:
            display_compressed(str, huffTable)
        elif opt == 5:
            results(str, binStr, huffTable)
        elif opt == 0:
            cont = False
        else:
            print("Invalid selection, please choose again.")

def display_compressed(str, huffTable):
    binStr = ""
    count = 0
    for c in str:
        for i in range(len(huffTable)):
            if c == huffTable[i][0]:
                print(huffTable[i][1], end = " ")
                count += len(huffTable[i][1])
                if count > 100:
                    print()
                    count = 0
    
def get_bin(a, str):
    binStr = ""
    for c in str:
        for x in a:
            if c == x[0]:
                binStr += x[1]
    return binStr

def results(str, binStr, huffTable):
    print("---------------Results---------------\n")
    print("Total Number of characters:", len(huffTable))
    print("Initial File Length:", len(str), "bytes")
    expLen = len(str) * math.ceil(math.log(len(huffTable), 2))
    print("Expected File Length: <", expLen, "bytes")
    print("Compressed File length", len(binStr) / 8, "bytes")

def print_freq(a):
    for x in a:
        print(str.format("{0}, {1:.5}", x[1], x[0]))
        
def print_table(a):
    for x in a:
        print(x)

if __name__ == '__main__':
    main()
    