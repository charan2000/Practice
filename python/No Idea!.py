n, m = map(int, input().split())
if(n>=1 and n<=10**5) and (m>=1 and m<=10**5):
    ar = list(map(int, input().split()))
    arr = []
    for i in ar:
        if(i>=1 and i<=10**9):
            arr.append(i)
    A, B = set(), set()
    s1 = set(map(int, input().split()))
    for i in s1:
        if(i>=1 and i<=10**9):
            A.add(i)
    s2 = set(map(int, input().split()))
    for i in s2:
        if(i>=1 and i<=10**9):
            B.add(i)
    hpy = 0
    for i in arr:
        if (i in A and i in B):
            hpy+=1
            hpy-=1
        elif (i in A ):
            hpy+=1
        elif(i in B):
            hpy-=1
    print(hpy)
