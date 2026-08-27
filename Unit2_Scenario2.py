def fib(n):
    if n <= 2:
        return n

    return fib(n-1) + fib(n-2)

n = int(input("Enter n: "))
table = [0] * (n+1)
table[0] = 0
table[1] = 1 
table[2] = 2
for i in range(3,n+1):
    table[i] = fib(i)

for i in table:
    print(i, end=" ")
