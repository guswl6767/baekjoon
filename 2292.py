import sys
sys.stdin = open("input.txt", "r")


n, m = map(int, input().split())
a = list(map(int, input().split()))
sum = []


for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            summ = a[i]+a[j]+a[k]
            if summ <= m:
                sum.append(summ)
print(max(sum))
