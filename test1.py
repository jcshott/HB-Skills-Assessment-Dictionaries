input_list = [1, 2, 3, -2, -1, 1, 1, 0]

sum_zero_pair_list = []
input_set = set(input_list)

#iterate through each number in the input list.  
for number in input_set:
#heather's suggested approach with sets but when i run outside this assignment as test, its fine, here i get 2 copies
    for next_number in input_set:
        if number + next_number == 0:
            sum_zero_pair_list.append((number, next_number))


#my way
#     for n in range(len(input_list) - input_list.index(number)): 
#         #create a tuple of each number plus every other number in the list, including itself, using index.
#         #the range is set up so that you won't get an index out of range error 
#         sum_pair_tuple = (number, input_list[input_list.index(number) + n]) 
    
#         #evaluate the current pair and if the first and last equal 0, put it in the dictionary as a key-value pair
#         if sum_pair_tuple[0] + sum_pair_tuple[1] == 0:
#             sum_zero_pair_dictionary[sum_pair_tuple[0]] = sum_pair_tuple[1]

# #to weed duplicate pairs (i.e. 1, -1 and -1,1), if a key is also a value, delete it. 
# #only exception is zero because it is the only number that you can add to itself to get zero
# for key in sum_zero_pair_dictionary.keys():
#     if key in sum_zero_pair_dictionary.values() and key != 0:
#         del sum_zero_pair_dictionary[key]

print sum_zero_pair_list
