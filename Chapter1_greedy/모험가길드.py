import sys
sys.stdin=open("input.txt" , "r")

n = int(input())
arr = list(map(int, input().split()))

cnt =0
result = 0

arr.sort()
for i in arr:
    cnt+=1
    if cnt >= i:
        result+=1
        cnt=0
print(result)