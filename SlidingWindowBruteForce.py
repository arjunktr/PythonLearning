//https://www.geeksforgeeks.org/window-sliding-technique/



def max_sub(list,number_of_elements):
    
    max_sum=0
    for counter in range(len(list)-number_of_elements+1):
        current_sum=0
        for inner_counter in range(number_of_elements):
            current_sum=current_sum+list[inner_counter+counter]
        if current_sum>max_sum:
            max_sum=current_sum
    return max_sum
    
list=[100,200,300,400]
print(max_sub(list,2))
