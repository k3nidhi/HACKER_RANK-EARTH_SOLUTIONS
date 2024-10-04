#!/bin/python3  

import sys  

# Function to calculate sum of multiples below n  
def sum_of_multiples_below(n, k):  
    p = (n - 1) // k  
    return k * p * (p + 1) // 2  


t = int(input().strip())  


for a0 in range(t):  
     
    n = int(input().strip())  
    
     
    sum_mult_3 = sum_of_multiples_below(n, 3)  
    
    
    sum_mult_5 = sum_of_multiples_below(n, 5)  
    
    
    sum_mult_15 = sum_of_multiples_below(n, 15)  
    
    
    sum_total = sum_mult_3 + sum_mult_5 - sum_mult_15  
    
    
    print(sum_total)
