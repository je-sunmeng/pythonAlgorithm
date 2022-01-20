def d(n):
    s = list(map(int, str(n)))
    return (n + sum(s))

N = 10000

a = list(range(N))
for i in range(0,N):
    a[i] = d(i)
a.sort()
for i in range(0,N):
    if(a.count(i) == 0):
        print(i)
