'''
understand: given a dictionary 
> keys are locations
> values are the integers

return the amount of total treasure

plan: 
could access all values then return the sum
> 
could also use a count variable and update that as I go. 

'''

#approach 1
#time complexity - 
# def total_treasures(treasure_map):
#     values = treasure_map.values()
#     return(sum(values))

# treasure_map1 = {
#     "Cove": 3,
#     "Beach": 7,
#     "Forest": 5
# }

# treasure_map2 = {
#     "Shipwreck": 10,
#     "Cave": 20,
#     "Lagoon": 15,
#     "Island Peak": 5
# }

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 


#problem 2
'''
understand: 
input: string called message
output: true if message contains every letter of alphabet at least once
false otherwise

plan:
have a lowercase alphabet set
make a set out of the message string
return if those sets are equal
'''

#time complexity : O(n)
# def can_trust_message(message):
#     lowercase = set('abcdefghijklmnopqrstuvwxyz')

#     test = set("".join([i for i in message if i != " "]))

#     return lowercase == test

# message1 = "sphinx of black quartz judge my vow"
# message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))



#problem 3 --- Find All Duplicate Treasure Chests in an Array

'''
understand: 
> input: array of integers
> output: array of the integers that have duplicates

plan: 
> can use a frequency dictionary
> if values are greater than 1 add a new list then return that list
'''

# def find_duplicate_chests(chests):
#     freq_dict = {}
#     for chest in chests:
#         if chest in freq_dict:
#             freq_dict[chest] += 1
#         else:
#             freq_dict[chest] = 1
    
#     duplicates = [] 
#     for key in freq_dict.keys():
#         if freq_dict[key] > 1:
#             duplicates.append(key)
    
#     return duplicates


# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))


#problem 4 -- booby trap
'''
understand:
balanced code = letters have equal frequency
disable: remove one letter to balance
> input: a string (the code) in lowercase. 
output: return true if one letter can be removed to make it balanced

plan
> could use a frequency dictionary again
> if the sum of the counts is greater than the length of the dictionary, then true
> otherwise false

'''

# def is_balanced(code):
#     freq_dict = {}
#     for char in code:
#         if char in freq_dict:
#             freq_dict[char] +=1
#         else:
#             freq_dict[char] = 1
    
#     if len(set(freq_dict.values())) == 1:
#         return False
#     else:
#         return True
    
# code1 = "arghhh"
# code2 = "haha"

# print(is_balanced(code1)) 
# print(is_balanced(code2)) 


#problem 5 - overflowing with Gold
'''
understand: need to find the indices that add up to the target

plan
- how to return list of indices 
    - use list.index()
> case 1: list has only two items. add items and if equal to target, return a list of the indices

> case 2: 
could use a double nested for loop
if lst[i] + lst[j] = target append both indices to index list


'''

def find_treasure_indices(gold_amounts, target):
    #remove numbers bigger than target
    amounts = []
    indices = []
    for gold in gold_amounts:
        if gold < target:
            amounts.append(gold)
    
    if len(amounts) == 2 and amounts[0]+amounts[1] == target:
        return [0,1]
    
    


