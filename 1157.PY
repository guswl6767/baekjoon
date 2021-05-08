import sys
sys.stdin = open("input.txt","r")


word = input()

if len(word) ==0:
    print(0)

else:
    print(word.count(' ')+1)