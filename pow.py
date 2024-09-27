def myPow(x: float, n: int):
    
    if n == 0:
        return 1
    
    
    if n < 0:
        return 1 / myPow(x, -n)
    
    
    half = myPow(x, n // 2)
    
    
    if n % 2 == 0:
        return half * half
    else:
        
        return half * half * x

 
print(myPow(2.00000, -2))
  
    






