#https://www.geeksforgeeks.org/window-sliding-technique/

def max_sub(list,n):
    
    current_sum=0
    for item in range(n):
        current_sum=current_sum+list[item]
        
    max_sum=current_sum    
    for item in range(len(list)-n):
        current_sum=current_sum+list[item+n]-list[item]
    
    if current_sum>max_sum:
        max_sum=current_sum
    return max_sum

list=[100,200,300,400]
print(max_sub(list,2))

