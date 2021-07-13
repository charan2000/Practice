from collections import Counter
lt=[]
n = int(input())
for _ in range(n):
    lt.append(input())
ctr = Counter(lt)
print(len(ctr))
print(*ctr.values())