def primefind2019_2_60_079(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True
n = int(input("enter the value:"))
print(primefind2019_2_60_079(n))
