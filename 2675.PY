import sys
sys.stdin = open("input.txt","r")


t= input().upper()
set_list = list(set(t))

cnt_list=[]
for x in set_list:
    cnt = t.count(x)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) >1 :
    print('?')

else:
    max_index= cnt_list.index(max(cnt_list))
    print(set_list[max_index])