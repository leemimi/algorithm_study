import sys
sys.stdin=open("input.txt", "r")

S = input()
Sr = list(str(S))

arr = list(map(int,Sr))

ans=0
for i in range(len(arr)):
    if arr[i] <=1 or ans <=1:
        ans +=arr[i]
    else:
        ans *=arr[i]
print(ans)