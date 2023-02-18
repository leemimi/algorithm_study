import sys
sys.stdin=open("input.txt", "r")

N,K = map(int,input().split())

result =0
while True:
    target = (N//K) * K
    result += (N-target)
    N = target
    if N<K:
        break
    result+=1
    N//=K
print(N)
result +=(N-1)
print(result)




