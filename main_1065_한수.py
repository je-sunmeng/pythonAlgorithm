def Len(n):
    s = list(map(int, str(n)))
    return len(s)

def Sub(n, i):
    s = list(map(int, str(n)))
    return (s[i] - s[i-1])

def main():
    N = int(input())
    count = 0
    for num in range(1, N+1):
        if(Len(num) <= 2):
            count += 1
        else:
            for i in range(1,Len(num)-1):
                if(Sub(num,i)-Sub(num,i+1) != 0):
                    break
                else:
                    count += 1

    print(count)

if __name__=="__main__":
    main()