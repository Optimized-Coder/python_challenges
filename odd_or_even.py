# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".

def odd_or_even(arr):
    arr_sum = sum(arr)
    print(arr_sum)
    if arr_sum % 2 == 0:
        print('even')
    else:
        print('odd')
        
# test
arr = [36, 35,13, 1]
odd_or_even(arr)
# prints 
>>> 85
>>> 'odd'
