def power(a, b, P): 
    if (b == 1): 
        return a 
    else:
        return ((pow(a, b)) % P)
G=9
a=4
b=3
P=29
print("P Value: ", P, "\n")  
print("G Value: ", G, "\n")
print("A Private KEY: ", a, "\n")
x = power(G, a, P)
print("The private key B: ", b, "\n")
y = power(G, b, P) 
ka = power(y, a, P) 
kb = power(x, b, P)
print("A Secret Key: ", ka, "\n") 
print("B Secret Key: ", kb, "\n")
