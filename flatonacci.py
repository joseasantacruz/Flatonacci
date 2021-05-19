"""
Flatonacci secuence is a secuence which is result from the same given secuence
plus the sum of the last 3 numbers of the secuence.
The challenge is to create a flatonacci function that given a signature returns the first
n elements - signature included of the so seeded sequence. So, if we are to
start our Flatonacci sequence with [1, 1, 1] as a starting input (AKA signature) and n = 8,
we have this sequence:
[1, 1 ,1, 3, 5, 9, 17, 31]
Another example; if signature is the secuence [0, 0, 1] we should get some thing
like:
[0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
- Signature will always contain 3 numbers
- n will always be a non-negative number
- if n == 0, then return an empty list and be ready for anything else which is not
clearly specified ;)
Note. Please note that we are gonna test the funcion against a lot of different signatures and n's
"""


def flatonacci(signature: list, n: int) -> list:
    # happy coding
    if len(signature)==3 and n>=0:
        result=[]
        a,b,c=signature[0],signature[1],signature[2]
        for i in range(n):
            if i==0:
                result.append(a)
            elif i==1:
                result.append(b)
            elif i==2:
                result.append(c)
            else:
                sum=a+b+c
                result.append(sum)
                a,b,c=b,c,sum
        return result
    else:
        return 'An error occurred in the parameters.'
print (flatonacci([1, 1, 1],8))
print (flatonacci([0, 0, 1],10))
print (flatonacci([-1, 1, -1],21))
