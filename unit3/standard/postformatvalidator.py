def is_valid_post_format(posts):
   stack = []
   for char in posts:
     if char in "({[":
       stack.append(char)
     else:
       if not stack:
        return False
       top = stack.pop()

       if char == ")" and top != "(":
        return False
       if char == "}" and top != "{":
        return False
       if char == "]" and top != "[":
        return False
   return len(stack) == 0


print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))