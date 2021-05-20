import sys
sys.stdin = open("input.txt","r")

a = ["c=","c-","dz=","d-","lj","nj","s=","z="]
n = input()
for i in a:
    n= n.replace(i, 'a')
print(len(n))