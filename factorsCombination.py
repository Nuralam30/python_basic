
from cgi import print_arguments


factors_combination = []
 
# recursive function
def compute_factors(current_no, n, product, single_list):
    global factors_combination
     
    # base case: if the product
    # exceeds our given number;
    # OR
    # current_no exceeds half the given n
    if ((current_no > int(n / 2)) or (product > n)):
        return
  
    # if current list of factors
    # is contributing to n
    if (product == n):
        # storing the list
        factors_combination.append(single_list)
         
        # printing all possible factors stored in
        # factors_combination
        for i in range(len(factors_combination)):
            for j in range(len(factors_combination[i])):
                print(factors_combination[i][j], end=" ")
        print()
        
        factors_combination = []
        # into factors_combination
        return
  
    # including current_no in our list
    single_list.append(current_no)
  
    # trying to get required
    # n with including current
    # current_no
    compute_factors(current_no, n, product * current_no, single_list)
  
    # excluding current_no from our list
    single_list.pop()
  
    # trying to get required n
    # without including current
    # current_no
    compute_factors(current_no + 1, n, product, single_list)
 
n = 24
 
# vector to store single list of factors
# eg. 2,2,2,2 is one of the list for n=16
single_list = []
 
# compute_factors ( starting_no, given_n,
# our_current_product, vector )
compute_factors(2, n, 1, single_list)
 