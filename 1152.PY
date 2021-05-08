import sys
sys.stdin = open("input.txt","r")


a ,b = input().split()
a = int(a[::-1])
b = int(b[::-1])   
                       """리스트 역순[::-1]"""
if a > b:
    print(a)

else:
    print(b)

