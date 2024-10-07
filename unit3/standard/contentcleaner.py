def clean_post(post):
  if len(post) <= 1:
    return post
  stack = []
  for char in post:
    if stack and ((char.islower() and char.upper()==stack[-1]) or(char.isupper() and char.lower()==stack[-1])):
          stack.pop()
    else:
       stack.append(char)
  return "".join(stack)

print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 