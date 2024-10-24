class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

tom_nook = Node("Tom Nook")
tommy = Node("Tommy") 
tom_nook.next = tommy 
print(tom_nook.value) 
print(tom_nook.next.value) 
print(tommy.value) 
print(tommy.next) 

timmy = Node("Timmy")
second = tom_nook.next
tom_nook.next = timmy
timmy.next = second

print(tom_nook.value)
print(tom_nook.next.value)
print(timmy.value)
print(timmy.next.value)
print(tommy.value)
print(tommy.next)


isabelle = Node("Isabelle")
saharah = Node("Saharah")
cj = Node("C.J.")

isabelle.next = saharah
saharah.next = cj

def print_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next
    
    

print(print_list(isabelle))