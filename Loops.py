# The provided code stub reads and integer,n , from STDIN. For all non-negative integers i < n, print i².

n = int(input())
if (n >=1 and n<=20):
    for i in list(range(n)):
        print (i**2)
