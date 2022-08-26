# Greatest common divisor (GCD) of two positive integers

x = int(input('Enter x: '))
y = int(input('Enter y: '))

def gcd(x,y):
    gcd = 1
    if x % y == 0:
        return y
    for k in range(int(y/2),0,-1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break
    return gcd

print("GCD of %d and %d is: " %(x,y), gcd(x,y) )
        

