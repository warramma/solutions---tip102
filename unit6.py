# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#      if not clues:
#          return False
     
#      first = clues

#      last = clues
#      while last and last.next:
#          last = last.next
#          if last == first:
#             return True
        
#      return False
     

# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))

##-------problem 2----breaking the cycle

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if not evidence:
        return []
    
    first = evidence
    last = evidence
    while last and last.next:
        first = first.next
        last = last.next.next
        if first == last:
            break
        
    else:
        return []
    
    

    #find start
    first = evidence
    while first!=last:
        first = first.next
        last = last.next
    
    #collect
    start = first
    current = start

    lst = []
    while True:
        lst.append(current.value)
        current = current.next
        if current == start:
            break
    
    return lst

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))



