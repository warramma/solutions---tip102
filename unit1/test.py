# #problem 1
# def reverse_sentence(sentence):
#     words = sentence.split()
#     if len(words) <= 1:
#         return sentence
#     reversed = " ".join(words[::-1])
#     #use join and then string traversla with splicing 

#     return reversed


# #don't name function and variable the same thing

# print(reverse_sentence("hello world it's me"))
# print(reverse_sentence("hello"))



#PROBLEM 3 - delete_minimum

# understand - -------------
# input - list of honey jar sizes
# output - sorted list, from smallest to greatest
# plan - -------------
# check if length of list is 1, then just return list as is
# initialize an empty list
# use a while loop to remove minimum from original list while not empty

def delete_minimum_elements(hunny_jar_sizes):
    remove_elements = []
    while hunny_jar_sizes:
        min_element = min(hunny_jar_sizes)
        hunny_jar_sizes.remove(min_element)
        remove_elements.append(min_element)

    return remove_elements

hunny_jar_sizes = [5, 3, 2, 4, 1]
print(delete_minimum_elements(hunny_jar_sizes))